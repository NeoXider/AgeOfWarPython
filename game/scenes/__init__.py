"""
Сцены игры.

Сцены — верхний уровень композиции (меню, игра и т.п.).
"""

from .game_scene import GameScene
from .menu_scene import MenuScene

__all__ = ["MenuScene", "GameScene"]

