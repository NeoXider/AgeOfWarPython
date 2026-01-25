"""
Сущность базы/замка.

Пока это каркас: примитивный спрайт и HP.
"""

from __future__ import annotations

from dataclasses import dataclass

import spritePro as s

from game.domain import BaseStats, Faction
from .entity import Entity


@dataclass(slots=True)
class Base(Entity):
    """База (цель, которую нужно разрушить)."""

    faction: Faction = Faction.PLAYER
    stats: BaseStats = BaseStats(max_hp=1000)
    hp: int = 1000

    @staticmethod
    def create(scene: s.Scene, faction: Faction, pos: tuple[float, float]) -> "Base":
        # Используем примитив (пустой путь к изображению), чтобы проект запускался без ассетов.
        sprite = s.Sprite(
            "",
            size=(120, 160),
            pos=pos,
            scene=scene,
            sorting_order=0,
        )
        sprite.color = (60, 180, 255) if faction == Faction.PLAYER else (255, 100, 100)
        base = Base(scene=scene, sprite=sprite, faction=faction, stats=BaseStats(max_hp=1000), hp=1000)
        return base

    def apply_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - max(0, amount))
        if self.hp <= 0:
            self.destroy()

