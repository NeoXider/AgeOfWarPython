"""
Домен игры (логика и данные без привязки к SpritePro).

Старайтесь держать здесь “правила” и модели, которые можно тестировать отдельно от рендера.
"""

from .economy import EconomyModel
from .enums import Age, Faction, UnitType
from .stats import BaseStats, UnitStats

__all__ = [
    "Age",
    "Faction",
    "UnitType",
    "UnitStats",
    "BaseStats",
    "EconomyModel",
]

