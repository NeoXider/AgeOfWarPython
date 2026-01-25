"""
Системы игры.

Система = отдельный блок логики, который обновляется сценой.
"""

from .battle_system import BattleSystem
from .economy_system import EconomySystem
from .spawn_system import SpawnSystem
from .system import System
from .ui_system import UISystem

__all__ = [
    "System",
    "EconomySystem",
    "SpawnSystem",
    "BattleSystem",
    "UISystem",
]

