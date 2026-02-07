from __future__ import annotations

from dataclasses import dataclass

import spritePro as s

from game.domain import Faction, UnitStats, UnitType
from .entity import Entity
from ..animation.first_warrior_animation import _build_animation


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
    target_x: float = 0.0
    is_moving: bool = False

    @staticmethod
    def create(scene: s.Scene, 
               faction: Faction, 
               pos: tuple[float, float], 
               unit_type: UnitType = UnitType.MELEE) -> "Unit":
        sprite = s.Sprite(
            "",
            size=(40, 40),
            pos=pos,
            scene=scene,
            sorting_order=5,
        )
        sprite.color = (30, 220, 120) if faction == Faction.PLAYER else (220, 60, 60)

        anim = _build_animation(sprite, unit_type)
        sprite.animation = anim
        anim.set_state('walk')  

        stats = UnitStats(
            unit_type=unit_type,
            max_hp=100,
            move_speed=120.0,
            attack_damage=10,
            attack_range=40.0,
            attack_cooldown=1.0,
        )

        unit = Unit(
            scene=scene,
            sprite=sprite,
            faction=faction,
            hp=100,
            stats=stats,
            target_x=pos[0],  
            )
        return unit

    def move_to(self, target_x: float) -> None:
        """Приказ юниту двигаться в позицию target_x."""
        self.target_x = target_x
        self.is_moving = True

    def update_movement(self, dt: float) -> None:
        """Обновление позиции юнита каждый кадр."""
        if not self.is_moving:
            return

        current_x = self.sprite.position[0]
        distance = self.target_x - current_x
        move_distance = self.stats.move_speed * dt

        if abs(distance) <= move_distance:
            self.sprite.position = (self.target_x, self.sprite.position[1])
            self.is_moving = False
        else:
            direction = 1 if distance > 0 else -1
            new_x = current_x + direction * move_distance
            self.sprite.position = (new_x, self.sprite.position [1])

    def apply_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - max(0, amount))
        if self.hp > 0:
            self.sprite.animation.set_state('hurt')  
        else:
            self.sprite.animation.set_state('dead')  
            self.destroy()