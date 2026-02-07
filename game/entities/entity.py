"""
Базовые сущности (Entity).

Entity — это "игровой объект": содержит ссылку на спрайт и состояние жизни.
"""

from __future__ import annotations

from dataclasses import dataclass
import spritePro as s


@dataclass(slots=True)
class Entity:
    """
    Базовая обёртка над игровым объектом.

    SpritePro сам отрисовывает спрайты, а эта обёртка помогает держать
    игровое состояние (hp/фракция/статы) рядом с визуалом.
    """

    scene: s.Scene
    sprite: s.Sprite
    is_alive: bool = True
    facing_dir: int = 1

    def destroy(self) -> None:
        if not self.is_alive:
            return
        self.is_alive = False
        try:
            self.sprite.set_active(False)
        except Exception:
            # На разных версиях SpritePro API может отличаться — делаем best-effort.
            pass

    def set_facing_dir(self, direction: int) -> None:
        """
        Выставляет направление взгляда сущности.

        Договор:
        - `+1` = смотреть вправо
        - `-1` = смотреть влево
        """
        direction = 1 if direction >= 0 else -1
        if self.facing_dir == direction:
            return
        self.facing_dir = direction
        self._apply_flip(flip_h=(direction < 0), flip_v=False)

    def face_left(self) -> None:
        """Сущность смотрит влево."""
        self.set_facing_dir(-1)

    def face_right(self) -> None:
        """Сущность смотрит вправо."""
        self.set_facing_dir(1)

    def face_towards_x(self, target_x: float) -> None:
        """Повернуть сущность в сторону X-координаты."""
        x = float(self.sprite.position[0])
        self.set_facing_dir(1 if target_x >= x else -1)

    def _apply_flip(self, *, flip_h: bool, flip_v: bool) -> None:
        """
        Применяет flip к спрайту и его детям.

        В SpritePro flip не наследуется автоматически, поэтому делаем это явно.
        """
        self.sprite.set_flip(flip_h=flip_h, flip_v=flip_v)
        for child in getattr(self.sprite, "children", []):
            try:
                child.set_flip(flip_h=flip_h, flip_v=flip_v)
            except Exception:
                pass

