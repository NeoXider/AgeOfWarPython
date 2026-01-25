"""
Точка входа в проект.

Держим `main.py` максимально тонким: создаём окно SpritePro, регистрируем сцены
и запускаем первую сцену по имени.
"""

import spritePro as s

import config
from game.scenes import GameScene, MenuScene


def main():
    s.get_screen(config.WINDOW_SIZE, "My SpritePro Game")
    s.enable_debug(True)
    s.set_debug_camera_input(3)
    s.debug_log_custom("CUSTOM","Game started", (255, 0, 255))
    s.scene.add_scene("menu", MenuScene)
    s.scene.add_scene("game", GameScene)
    s.set_scene_by_name("menu")

    while True:
        s.update(config.FPS, fill_color=(20, 20, 30))


if __name__ == "__main__":
    main()
