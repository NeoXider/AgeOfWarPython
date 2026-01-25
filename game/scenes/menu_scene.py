"""
Сцена меню.

Отвечает за старт/выход и (в будущем) настройки/выбор режима.
"""

from __future__ import annotations

import spritePro as s


class MenuScene(s.Scene):
    """Главное меню проекта."""

    def __init__(self) -> None:
        super().__init__()

        # Заголовок
        self._title = s.TextSprite(
            "Age of War (Scaffold)",
            48,
            (255, 255, 255),
            (s.WH_C.x, 120),
            anchor=s.Anchor.CENTER,
            sorting_order=1000,
            scene=self,
        )
        self._title.set_screen_space(True)

        def start_game() -> None:
            # Переходим в игровую сцену по имени (как в референсе SpritePro).
            # recreate=True — чтобы каждый запуск начинался "с нуля".
            s.set_scene_by_name("game", recreate=True)

        self._start_btn = s.Button(
            "",
            (260, 60),
            (s.WH_C.x, s.WH_C.y),
            "Start",
            32,
            on_click=start_game,
            scene=self,
        )
        self._start_btn.set_screen_space(True)

        def quit_game() -> None:
            # Для учебного каркаса достаточно поднять SystemExit.
            raise SystemExit(0)

        self._quit_btn = s.Button(
            "",
            (260, 60),
            (s.WH_C.x, s.WH_C.y + 90),
            "Quit",
            32,
            on_click=quit_game,
            scene=self,
        )
        self._quit_btn.set_screen_space(True)

    def on_enter(self, context) -> None:
        # Ничего не выключаем: debug-камера управляется глобально через `main.py`.
        pass

    def on_exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

