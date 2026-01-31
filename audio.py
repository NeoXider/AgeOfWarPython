"""
Звук (устаревший модуль).

Сейчас в проекте предпочтительный путь — работать со звуком через `spritePro.audio_manager`
и события/системы. Этот файл оставлен для совместимости и примеров.
"""
from random import choice
import spritePro as s
from game.paths import PATHS
def play_attack_sound():
    list_random_hit_sound  = ['/Blow1.ogg','/Blow2.ogg','/Blow3.ogg',]
    audio_hit = PATHS.audio + choice(list_random_hit_sound)
    s.audio_manager.play_sound(audio_hit)

def play_music_game():
    """Запустить фоновую музыку (если файл существует)."""
    s.audio_manager.play_music(PATHS.audio+'/Dungeon1.ogg',-1,0.3)

def stop_music():
    """Остановить фоновую музыку."""
    s.audio_manager.stop_music()

