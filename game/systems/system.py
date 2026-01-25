"""
Базовые типы для систем.

Система — это объект, который обновляется сценой каждый кадр.
"""

from __future__ import annotations

from typing import Protocol


class System(Protocol):
    """
    Минимальный “контракт” системы.

    Система — это небольшой модуль логики, который обновляется сценой каждый кадр.
    Важно: система не владеет игровым циклом; сцене принадлежит управление.
    """

    def on_enter(self) -> None: ...
    def on_exit(self) -> None: ...
    def update(self, dt: float) -> None: ...

