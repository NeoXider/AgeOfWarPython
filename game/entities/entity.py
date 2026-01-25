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

    def destroy(self) -> None:
        if not self.is_alive:
            return
        self.is_alive = False
        try:
            self.sprite.set_active(False)
        except Exception:
            # На разных версиях SpritePro API может отличаться — делаем best-effort.
            pass

