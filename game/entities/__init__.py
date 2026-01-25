"""
Сущности игры (игровые объекты).

Entity-обёртки помогают держать состояние рядом со SpritePro-спрайтами.
"""

from .base import Base
from .entity import Entity
from .projectile import Projectile
from .unit import Unit

__all__ = ["Entity", "Base", "Unit", "Projectile"]

