"""
Система боя (каркас).

Здесь позже появится логика выбора целей, кулдауны атак и нанесение урона.
"""

from __future__ import annotations

from typing import List

from game.entities import Projectile, Unit


class BattleSystem:
    """
    Каркас системы боя.

    Что будет здесь позже (пока не реализовано):
    - выбор цели (ближайший враг в lane)
    - кулдауны атак
    - применение урона
    - создание снарядов для дальников
    """

    def __init__(self, events, *, units: List[Unit], projectiles: List[Projectile]) -> None:
        # events: spritePro EventBus (обычно s.events)
        self._events = events
        self._units = units
        self._projectiles = projectiles

    def on_enter(self) -> None:
        pass

    def on_exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        # намеренно пусто: это каркас
        pass

