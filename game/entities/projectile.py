"""
Сущность снаряда.

Пока это каркас: примитивный спрайт, скорость и урон.
"""

from __future__ import annotations

from dataclasses import dataclass

import spritePro as s

from game.domain import Faction
from .entity import Entity


@dataclass(slots=True)
class Projectile(Entity):
    """Снаряд (для дальних атак)."""

    faction: Faction = Faction.PLAYER
    damage: int = 10
    speed: float = 240.0

    @staticmethod
    def create(scene: s.Scene, faction: Faction, pos: tuple[float, float]) -> "Projectile":
        sprite = s.Sprite(
            "",
            size=(12, 6),
            pos=pos,
            scene=scene,
            sorting_order=10,
        )
        sprite.color = (250, 230, 80)
        return Projectile(scene=scene, sprite=sprite, faction=faction)

