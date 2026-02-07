"""
Игровая сцена.

Содержит объекты мира и список систем, которые обновляются каждый кадр.
"""

from __future__ import annotations

import pygame
import spritePro as s
from audio import play_music_game,stop_music
from game.domain import EconomyModel, Faction
from game.entities import Base, Projectile, Unit
from game.global_events import GameEvents, SpawnRequested
from game.systems import BattleSystem, EconomySystem, SpawnSystem, UISystem


class GameScene(s.Scene):
    """Основная игровая сцена (мир + HUD)."""

    def __init__(self) -> None:
        super().__init__()
        # Используем встроенный EventBus из SpritePro (глобальный).
        self.events = s.events
        
        # Состояние сцены
        self.units: list[Unit] = []
        self.projectiles: list[Projectile] = []

        self.economy = EconomyModel(
            gold={Faction.PLAYER: 0, Faction.ENEMY: 0},
            income_per_second={Faction.PLAYER: 5, Faction.ENEMY: 5},
        )

        # Создаём объекты мира в конструкторе (как договорились в проекте).
        self.player_base = Base.create(self, Faction.PLAYER, (50, 360))
        self.enemy_base = Base.create(self, Faction.ENEMY, (850, 360))

        # Создаём системы в конструкторе, подписки/ресурсы включаем в on_enter.
        self.systems = [
            EconomySystem(self.events, self.economy, scene=self),
            SpawnSystem(self.events, units=self.units, scene=self),
            BattleSystem(self.events, units=self.units, projectiles=self.projectiles),
            UISystem(self.events, scene=self),
        ]

    def on_enter(self, context) -> None:
        for sys in self.systems:
            sys.on_enter()
        play_music_game()

    def on_exit(self) -> None:
        for sys in reversed(self.systems):
            sys.on_exit()
        stop_music()

    def update(self, dt: float) -> None:
        # Пример: запрос спавна через событие (демонстрация event-driven подхода)
        if s.input.was_pressed(pygame.K_1):
            self.events.send(GameEvents.UNIT_SPAWN_REQUESTED, data=SpawnRequested(faction=Faction.PLAYER))
        if s.input.was_pressed(pygame.K_2):
            self.events.send(GameEvents.UNIT_SPAWN_REQUESTED, data=SpawnRequested(faction=Faction.ENEMY))
        if s.input.was_pressed(pygame.K_3):
            if self.units:
                self.units[0].move_to(400.0)

        for unit in self.units:
            unit.update_movement(dt)
        for sys in self.systems:
            sys.update(dt)

