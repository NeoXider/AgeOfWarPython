"""
Система экономики.

Отвечает за начисление золота и рассылку события об изменении золота.
"""

from __future__ import annotations

from game.domain import EconomyModel, Faction
from game.global_events import GameEvents, GoldChanged


class EconomySystem:
    """
    Каркас системы экономики: начисляет золото по времени и эмитит событие.
    """

    def __init__(self, events, economy: EconomyModel, tick_seconds: float = 1.0) -> None:
        # events: spritePro EventBus (обычно s.events)
        self._events = events
        self._economy = economy
        self._tick_seconds = max(0.05, tick_seconds)
        self._acc = 0.0

    def on_enter(self) -> None:
        self._acc = 0.0

    def on_exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        self._acc += max(0.0, dt)
        while self._acc >= self._tick_seconds:
            self._acc -= self._tick_seconds
            for faction in (Faction.PLAYER, Faction.ENEMY):
                delta = int(self._economy.income_per_second.get(faction, 0))
                if delta == 0:
                    continue
                new_gold = self._economy.add_gold(faction, delta)
                self._events.send(
                    GameEvents.GOLD_CHANGED,
                    data=GoldChanged(faction=faction, new_gold=new_gold, delta=delta),
                )

