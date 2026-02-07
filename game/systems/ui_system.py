"""
Система UI/HUD.

Создаёт screen-space UI и связывает его с механиками через события.
"""

from __future__ import annotations

from typing import Optional

import spritePro as s

from game.domain import Faction, UnitType
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
        self._gold_iface: Optional[s.Sprite] = None
        self.panel_spawn: Optional[s.Sprite] = None
        self._spawn_player_melee_btn: Optional[s.Button] = None
        self._spawn_player_ranged_btn: Optional[s.Button] = None
        self._spawn_enemy_melee_btn: Optional[s.Button] = None
        self._spawn_enemy_ranged_btn: Optional[s.Button] = None
        self._gold_player: int = 0
        self._gold_enemy: int = 0

    def on_enter(self) -> None:
        self._gold_iface = s.Sprite(
            "assets/images/left_burda.png",
            (350,150),
            (-55, 0),
            0,
            anchor=s.Anchor.TOP_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._gold_iface.set_screen_space(True)

        self._gold_text = s.TextSprite(
            "Gold: 0 | Enemy: 0",
            28,
            (0, 0, 0),
            (20, 50),
            anchor=s.Anchor.TOP_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._gold_text.set_screen_space(True)

        def spawn_player_melee() -> None:
            self._events.send(
                GameEvents.UNIT_SPAWN_REQUESTED,
                data=SpawnRequested(faction=Faction.PLAYER, unit_type=UnitType.MELEE),
            )

        self.panel_spawn = s.Sprite(
            "assets/images/right_burda.png",
            (500,300),
            (900, -100),
            0,
            anchor=s.Anchor.TOP_RIGHT,
            sorting_order=1000,
            scene=self._scene,
        )
        self.panel_spawn.set_screen_space(True)

        self._spawn_player_melee_btn = s.Button(
            'assets/images/death.png',
            (48, 48),
            (50,0),
            "",
            22,
            on_click=spawn_player_melee,
            anchor=s.Anchor.BOTTOM_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._spawn_player_melee_btn.set_parent(self.panel_spawn,False)
        self._spawn_player_melee_btn.local_position = (-100,10)
        

        def spawn_player_ranged() -> None:
            self._events.send(
                GameEvents.UNIT_SPAWN_REQUESTED,
                data=SpawnRequested(faction=Faction.PLAYER, unit_type=UnitType.RANGED),
            )

        self._spawn_player_ranged_btn = s.Button(
            'assets/images/piupiu.png',
            (48, 48),
            (50,0),
            "",
            22,
            on_click=spawn_player_ranged,
            anchor=s.Anchor.BOTTOM_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._spawn_player_ranged_btn.set_parent(self.panel_spawn,False)
        self._spawn_player_ranged_btn.local_position = (-50,10)

        def spawn_enemy_melee() -> None:
            self._events.send(
                GameEvents.UNIT_SPAWN_REQUESTED,
                data=SpawnRequested(faction=Faction.ENEMY, unit_type=UnitType.MELEE),
            )

        self._spawn_enemy_melee_btn = s.Button(
            "",
            (220, 48),
            (470, s.WH.y - 20),
            "E: MELEE (2)",
            22,
            on_click=spawn_enemy_melee,
            anchor=s.Anchor.BOTTOM_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._spawn_enemy_melee_btn.set_screen_space(True)

        def spawn_enemy_ranged() -> None:
            self._events.send(
                GameEvents.UNIT_SPAWN_REQUESTED,
                data=SpawnRequested(faction=Faction.ENEMY, unit_type=UnitType.RANGED),
            )

        self._spawn_enemy_ranged_btn = s.Button(
            "",
            (220, 48),
            (700, s.WH.y - 20),
            "E: RANGED (4)",
            22,
            on_click=spawn_enemy_ranged,
            anchor=s.Anchor.BOTTOM_LEFT,
            sorting_order=1000,
            scene=self._scene,
        )
        self._spawn_enemy_ranged_btn.set_screen_space(True)

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
        if self._spawn_player_melee_btn:
            try:
                self._spawn_player_melee_btn.set_active(False)
            except Exception:
                pass
            self._spawn_player_melee_btn = None
        if self._spawn_player_ranged_btn:
            try:
                self._spawn_player_ranged_btn.set_active(False)
            except Exception:
                pass
            self._spawn_player_ranged_btn = None
        if self._spawn_enemy_melee_btn:
            try:
                self._spawn_enemy_melee_btn.set_active(False)
            except Exception:
                pass
            self._spawn_enemy_melee_btn = None
        if self._spawn_enemy_ranged_btn:
            try:
                self._spawn_enemy_ranged_btn.set_active(False)
            except Exception:
                pass
            self._spawn_enemy_ranged_btn = None

    def update(self, dt: float) -> None:
        pass

    def _on_gold_changed(self, *, data: GoldChanged) -> None:
        if data.faction == Faction.PLAYER:
            self._gold_player = data.new_gold
        else:
            self._gold_enemy = data.new_gold
        if self._gold_text:
            self._gold_text.set_text(f"Gold: {self._gold_player} | Enemy: {self._gold_enemy}")

