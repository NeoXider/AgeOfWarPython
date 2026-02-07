"""
Пути проекта.

Это “единая точка правды” для папок ассетов и других путей.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Paths:
    """
    Единый источник путей проекта.

    Правило: не хардкодим строки вида \"assets/...\" по проекту.
    Если появилась новая папка — добавляем поле сюда и используем `PATHS.*`.
    """

    assets: str = "assets"
    images: str = "assets/images"
    audio: str = "assets/audio"
    images_warrior: str = "assets/images/Warriors"

PATHS = Paths()

