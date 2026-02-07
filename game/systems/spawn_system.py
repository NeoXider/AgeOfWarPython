"""
Система спавна юнитов.

Подписывается на событие запроса спавна и создаёт юнитов в сцене.
"""

from __future__ import annotations

from typing import List, TYPE_CHECKING

from game.domain import Faction
from game.entities import Unit
from game.global_events import GameEvents, SpawnRequested

if TYPE_CHECKING:
    import spritePro as s
    from game.entities import Unit

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
        for u in self._units:
            desired_x = 850.0 if u.faction == Faction.PLAYER else 50.0
            if u.is_alive and u.target_x != desired_x:
                u.move_to(desired_x)

    def _on_spawn_requested(self, *, data: SpawnRequested) -> None:
        x = 135 if data.faction == Faction.PLAYER else 790
        y = 380
        u = Unit.create(self._scene, data.faction, (x, y), unit_type=data.unit_type)
        self._units.append(u)

