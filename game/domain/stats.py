"""
Характеристики (статы) игровых сущностей.

Старайтесь хранить числовой баланс в dataclass-ах, а не размазывать по логике.
"""

from __future__ import annotations

from dataclasses import dataclass

from .enums import UnitType


@dataclass(frozen=True, slots=True)
class UnitStats:
    """Характеристики юнита."""

    unit_type: UnitType
    max_hp: int
    move_speed: float
    attack_damage: int
    attack_range: float
    attack_cooldown: float


@dataclass(frozen=True, slots=True)
class BaseStats:
    """Характеристики базы/замка."""

    max_hp: int

