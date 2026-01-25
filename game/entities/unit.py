"""
Сущность юнита.

Пока это каркас: примитивный спрайт, статы и HP.
"""

from __future__ import annotations

from dataclasses import dataclass

import spritePro as s

from game.domain import Faction, UnitStats, UnitType
from .entity import Entity


@dataclass(slots=True)
class Unit(Entity):
    """Юнит (боевой объект на линии)."""

    faction: Faction = Faction.PLAYER
    stats: UnitStats = UnitStats(
        unit_type=UnitType.MELEE,
        max_hp=100,
        move_speed=120.0,
        attack_damage=10,
        attack_range=40.0,
        attack_cooldown=1.0,
    )
    hp: int = 100

    @staticmethod
    def create(scene: s.Scene, faction: Faction, pos: tuple[float, float]) -> "Unit":
        sprite = s.Sprite(
            "",
            size=(40, 40),
            pos=pos,
            scene=scene,
            sorting_order=5,
        )
        sprite.color = (30, 220, 120) if faction == Faction.PLAYER else (220, 60, 60)
        unit = Unit(scene=scene, sprite=sprite, faction=faction, hp=100)
        return unit

    def apply_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - max(0, amount))
        if self.hp <= 0:
            self.destroy()

