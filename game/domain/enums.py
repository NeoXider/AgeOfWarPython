"""
Перечисления домена (чистая логика игры).

Здесь лежат типы, которые используются по всему проекту и не зависят от SpritePro.
"""

from __future__ import annotations

from enum import Enum


class Faction(str, Enum):
    """Сторона конфликта."""

    PLAYER = "player"
    ENEMY = "enemy"


class Age(str, Enum):
    """Эпоха (прогресс развития)."""

    STONE = "stone"
    MEDIEVAL = "medieval"
    MODERN = "modern"


class UnitType(str, Enum):
    """
    Тип юнита по роли.

    - MELEE: ближний бой
    - RANGED: дальний бой
    - SIEGE: осадный юнит (катапульта/таран/пушка): обычно медленный и дорогой,
      но с сильным уроном по базе/строениям.
    """

    MELEE = "melee"
    RANGED = "ranged"
    SIEGE = "siege"




