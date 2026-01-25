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
        # Создаём UI-объекты в конструкторе (как договорились в проекте).
        # Важно: `main.py` вызывает `get_screen()` до регистрации сцен, поэтому `s.WH/s.WH_C` уже валидны.

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

        # Изначально выключаем, включаем в on_enter.
        self._title.set_active(False)
        self._start_btn.set_active(False)
        self._quit_btn.set_active(False)

    def on_enter(self, context) -> None:
        # В меню отключаем управление debug-камерой, чтобы UI не "плавал" без screen-space вызовов в сценах.
        s.set_debug_camera_input(None)

        self._title.set_active(True)
        self._start_btn.set_active(True)
        self._quit_btn.set_active(True)

    def on_exit(self) -> None:
        self._title.set_active(False)
        self._start_btn.set_active(False)
        self._quit_btn.set_active(False)

    def update(self, dt: float) -> None:
        pass

