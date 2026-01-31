"""
Звук (устаревший модуль).

Сейчас в проекте предпочтительный путь — работать со звуком через `spritePro.audio_manager`
и события/системы. Этот файл оставлен для совместимости и примеров.
"""

import spritePro as s
from game.paths import PATHS
attack_sound:s.Sound = s.load_sound('attack',PATHS.audio +'/Blow1.ogg')

def play_music_game():
    """Запустить фоновую музыку (если файл существует)."""
    s.audio_manager.play_music(PATHS.audio+'/Dungeon1.ogg',-1,0.3)

def stop_music():
    """Остановить фоновую музыку."""
    s.audio.stop_music()

