"""
Юнит (Entity) — боевой объект на линии.

Здесь живут:
- создание спрайта и привязка анимаций
- простейшее движение по X
- выставление направления (flip) по движению, чтобы враги не шли “задом”
"""

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
        #sprite.color = (30, 220, 120) if faction == Faction.PLAYER else (220, 60, 60)

        if unit_type == UnitType.SIEGE:
            sprite.scale = 0.5

        anim = _build_animation(sprite, unit_type)
        sprite.animation = anim
        anim.set_state("walk")
        anim.play()

        stats = _stats_for(unit_type)

        unit = Unit(
            scene=scene,
            sprite=sprite,
            faction=faction,
            hp=stats.max_hp,
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
        self._sync_walk_state()

        if not self.is_moving:
            return

        current_x = self.sprite.position[0]
        distance = self.target_x - current_x
        move_distance = self.stats.move_speed * dt
        self.set_facing_dir(1 if distance >= 0 else -1)

        if abs(distance) <= move_distance:
            self.sprite.position = (self.target_x, self.sprite.position[1])
            self.is_moving = False
        else:
            direction = 1 if distance > 0 else -1
            new_x = current_x + direction * move_distance
            self.sprite.position = (new_x, self.sprite.position[1])

    def apply_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - max(0, amount))
        if self.hp > 0:
            self.sprite.animation.set_state("hurt")
            self.sprite.animation.play()
        else:
            self.sprite.animation.set_state("dead")
            self.sprite.animation.play()
            self.destroy()

    def _sync_walk_state(self) -> None:
        """Ставит walk/idle в зависимости от движения, не сбрасывая кадр каждый тик."""
        anim = getattr(self.sprite, "animation", None)
        if anim is None:
            return
        if getattr(anim, "current_state", None) in ("hurt", "dead"):
            return

        desired = "walk" if self.is_moving else "idle"
        if getattr(anim, "current_state", None) != desired:
            anim.set_state(desired)
            anim.play()


def _stats_for(unit_type: UnitType) -> UnitStats:
    """Возвращает характеристики для конкретного типа юнита."""
    if unit_type == UnitType.MELEE:
        return UnitStats(
            unit_type=unit_type,
            max_hp=120,
            move_speed=140.0,
            attack_damage=12,
            attack_range=40.0,
            attack_cooldown=0.9,
        )
    if unit_type == UnitType.RANGED:
        return UnitStats(
            unit_type=unit_type,
            max_hp=80,
            move_speed=120.0,
            attack_damage=8,
            attack_range=180.0,
            attack_cooldown=1.2,
        )
    return UnitStats(
        unit_type=unit_type,
        max_hp=200,
        move_speed=90.0,
        attack_damage=20,
        attack_range=120.0,
        attack_cooldown=2.0,
    )