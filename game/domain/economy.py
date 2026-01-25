"""
Экономика (доменная модель).

Здесь только данные и простые правила (прибавить/потратить), без UI и без SpritePro.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .enums import Faction


@dataclass(slots=True)
class EconomyModel:
    """
    Минимальная модель экономики.

    Для учебного каркаса держим предельно простой набор правил:
    золото, доход, траты.
    """

    gold: Dict[Faction, int]
    income_per_second: Dict[Faction, int]

    def add_gold(self, faction: Faction, delta: int) -> int:
        self.gold[faction] = max(0, self.gold.get(faction, 0) + delta)
        return self.gold[faction]

    def can_spend(self, faction: Faction, amount: int) -> bool:
        return self.gold.get(faction, 0) >= amount

    def spend(self, faction: Faction, amount: int) -> bool:
        if not self.can_spend(faction, amount):
            return False
        self.gold[faction] -= amount
        return True

    def income_tick(self, faction: Faction, dt: float) -> int:
        # Учебная упрощённая модель: целочисленный доход в секунду.
        return self.income_per_second.get(faction, 0)

