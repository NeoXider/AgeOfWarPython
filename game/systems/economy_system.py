"""
Система экономики.

Отвечает за начисление золота и рассылку события об изменении золота.
"""

from __future__ import annotations

import spritePro as s

from game.domain import EconomyModel, Faction
from game.global_events import GameEvents, GoldChanged


class EconomySystem:
    """
    Каркас системы экономики: начисляет золото по времени и эмитит событие.
    """

    def __init__(
        self,
        events,
        economy: EconomyModel,
        scene,
        tick_seconds: float = 1.0,
    ) -> None:
        """
        Args:
            events: Глобальный EventBus из SpritePro (обычно `s.events`).
            economy: Доменная модель экономики.
            scene: Сцена, в которой активен таймер (SpritePro проверяет активность сцены).
            tick_seconds: Период начисления (в секундах).
        """
        self._events = events
        self._economy = economy
        self._tick_seconds = max(0.05, float(tick_seconds))

        # Таймер автоматически регистрируется в SpritePro и обновляется каждый кадр.
        # Параметр scene гарантирует, что начисление будет идти только в активной сцене.
        self._timer = s.Timer(
            self._tick_seconds,
            callback=self._on_tick,
            repeat=True,
            autostart=False,
            auto_register=True,
            use_dt=True,
            scene=scene,
        )

    def on_enter(self) -> None:
        self._timer.start(self._tick_seconds)

    def on_exit(self) -> None:
        self._timer.stop()

    def update(self, dt: float) -> None:
        pass

    def _on_tick(self) -> None:
        """Начисляет золото раз в тик и рассылает событие."""
        for faction in (Faction.PLAYER, Faction.ENEMY):
            delta = int(self._economy.income_per_second.get(faction, 0))
            if delta == 0:
                continue
            new_gold = self._economy.add_gold(faction, delta)
            self._events.send(
                GameEvents.GOLD_CHANGED,
                data=GoldChanged(faction=faction, new_gold=new_gold, delta=delta),
            )

