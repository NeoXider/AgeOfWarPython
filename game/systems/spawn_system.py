"""
Система спавна юнитов.

Подписывается на событие запроса спавна и создаёт юнитов в сцене.
"""

from __future__ import annotations

from typing import List, Optional

from game.domain import Faction
from game.entities import Unit
from game.global_events import GameEvents, SpawnRequested


class SpawnSystem:
    """
    Каркас системы спавна.

    Сейчас это демонстрация событийного подхода:
    UI/ввод эмитит событие, а спавн делает всё остальное.
    """

    def __init__(self, events, *, units: List[Unit], scene) -> None:
        # events: spritePro EventBus (обычно s.events)
        self._events = events
        self._units = units
        self._scene = scene
        self._connected_handler = None

    def on_enter(self) -> None:
        self._connected_handler = self._on_spawn_requested
        self._events.connect(GameEvents.UNIT_SPAWN_REQUESTED, self._connected_handler)

    def on_exit(self) -> None:
        if self._connected_handler is not None:
            self._events.disconnect(GameEvents.UNIT_SPAWN_REQUESTED, self._connected_handler)
            self._connected_handler = None

    def update(self, dt: float) -> None:
        pass

    def _on_spawn_requested(self, *, data: SpawnRequested) -> None:
        x = 180 if data.faction == Faction.PLAYER else 620
        y = 380
        unit = Unit.create(self._scene, data.faction, (x, y))
        self._units.append(unit)

