"""
Глобальные события проекта.

SpritePro уже имеет EventBus (`s.events`), а этот файл — “словарь” событий:
имена + типизированные payload (dataclass).

Договор проекта:
- отправляем так: `s.events.send(GameEvents.X, data=Payload(...))`
- принимаем так: `def handler(self, *, data: Payload): ...`

Справка по именованию событий:
- `aow` = namespace проекта **Age Of War** (чтобы не пересекаться с `spritePro` и чужими демо/модулями)
- формат: `aow.<подсистема>.<действие>`
- события-факты (что уже произошло): `...changed`, `...spawned`, `...killed`
- события-запросы (просим систему что-то сделать): `...requested`
"""

from __future__ import annotations

from dataclasses import dataclass

from game.domain import Faction


class GameEvents:
    """
    Глобальные события проекта (единый список).

    Важно:
    - В SpritePro события передаются как **kwargs.
    - В этом проекте договор: всегда передаём payload в аргументе `data`.
      Пример: `s.events.send(GameEvents.GOLD_CHANGED, data=GoldChanged(...))`
    """

    # Примеры:
    # - aow.gold.changed: золото изменилось (факт)
    # - aow.unit.spawn_requested: запросить спавн юнита (запрос)
    GOLD_CHANGED = "aow.gold.changed"
    UNIT_SPAWN_REQUESTED = "aow.unit.spawn_requested"


@dataclass(frozen=True, slots=True)
class GoldChanged:
    faction: Faction
    new_gold: int
    delta: int


@dataclass(frozen=True, slots=True)
class SpawnRequested:
    faction: Faction
    lane: int = 0

