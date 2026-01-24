import pygame
import spritePro as s

ASSETS_DIR = "assets"
IMAGES_DIR = f"{ASSETS_DIR}/images"
AUDIO_DIR = f"{ASSETS_DIR}/audio"


class MainScene(s.Scene):
    def __init__(self):
        super().__init__()
        self.player = s.Sprite(
            f"{IMAGES_DIR}/player.png",
            (64, 64),
            (400, 300),
            speed=5,
            scene=self,
        )

    def on_enter(self, context):
        pass

    def on_exit(self):
        pass

    def update(self, dt):
        self.player.handle_keyboard_input()
        if s.input.was_pressed(pygame.K_SPACE):
            s.debug_log_info("Space pressed")
