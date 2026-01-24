import spritePro as s

import config
from scenes.main_scene import MainScene


def main():
    s.get_screen(config.WINDOW_SIZE, "My SpritePro Game")
    s.enable_debug(True)
    s.set_debug_camera_input(3)
    s.debug_log_custom("CUSTOM","Game started", (255, 0, 0))
    s.set_scene(MainScene())

    while True:
        s.update(config.FPS, fill_color=(20, 20, 30))


if __name__ == "__main__":
    main()
