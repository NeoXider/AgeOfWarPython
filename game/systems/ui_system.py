"""
Система UI/HUD.

Создаёт screen-space UI и связывает его с механиками через события.
"""

from __future__ import annotations

from typing import Optional

import spritePro as s

from game.domain import Faction
from game.global_events import GameEvents, GoldChanged, SpawnRequested


class UISystem:
    """
    Минимальный каркас HUD (screen-space).

    В реальном проекте HUD лучше дробить на виджеты, но в учебном каркасе
    оставляем всё максимально явно и компактно.
    """

    def __init__(self, events, *, scene: s.Scene) -> None:
        # events: spritePro EventBus (обычно s.events)
        self._events = events
        self._scene = scene
        self._gold_handler: Optional[callable] = None
        self._gold_text: Optional[s.TextSprite] = None
        self._spawn_player_btn: Optional[s.Button] = None
        self._spawn_enemy_btn: Optional[s.Button] = None
        self._gold_player: int = 0
        self._gold_enemy: int = 0

    def on_enter(self) -> None:
        self._gold_text = s.TextSprite(
            "Gold: 0 | Enemy: 0",
            28,
            (255, 255, 255),
            (10, 10),
            anchor=s.Anchor.TOP_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._gold_text.set_screen_space(True)

        def spawn_player() -> None:
            self._events.send(
                GameEvents.UNIT_SPAWN_REQUESTED,
                data=SpawnRequested(faction=Faction.PLAYER),
            )

        self._spawn_player_btn = s.Button(
            "",
            (220, 48),
            (10, s.WH.y - 20),
            "Spawn Player (1)",
            22,
            on_click=spawn_player,
            anchor=s.Anchor.BOTTOM_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._spawn_player_btn.set_screen_space(True)

        def spawn_enemy() -> None:
            self._events.send(
                GameEvents.UNIT_SPAWN_REQUESTED,
                data=SpawnRequested(faction=Faction.ENEMY),
            )

        self._spawn_enemy_btn = s.Button(
            "",
            (220, 48),
            (240, s.WH.y - 20),
            "Spawn Enemy (2)",
            22,
            on_click=spawn_enemy,
            anchor=s.Anchor.BOTTOM_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._spawn_enemy_btn.set_screen_space(True)

        self._events.connect(GameEvents.GOLD_CHANGED, self._on_gold_changed)
        self._gold_handler = self._on_gold_changed

    def on_exit(self) -> None:
        if self._gold_handler:
            self._events.disconnect(GameEvents.GOLD_CHANGED, self._gold_handler)
            self._gold_handler = None
        if self._gold_text:
            try:
                self._gold_text.set_active(False)
            except Exception:
                pass
            self._gold_text = None
        if self._spawn_player_btn:
            try:
                self._spawn_player_btn.set_active(False)
            except Exception:
                pass
            self._spawn_player_btn = None
        if self._spawn_enemy_btn:
            try:
                self._spawn_enemy_btn.set_active(False)
            except Exception:
                pass
            self._spawn_enemy_btn = None

    def update(self, dt: float) -> None:
        pass

    def _on_gold_changed(self, *, data: GoldChanged) -> None:
        if data.faction == Faction.PLAYER:
            self._gold_player = data.new_gold
        else:
            self._gold_enemy = data.new_gold
        if self._gold_text:
            self._gold_text.set_text(f"Gold: {self._gold_player} | Enemy: {self._gold_enemy}")

