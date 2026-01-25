"""
Звук (устаревший модуль).

Сейчас в проекте предпочтительный путь — работать со звуком через `spritePro.audio_manager`
и события/системы. Этот файл оставлен для совместимости и примеров.
"""

import spritePro as s

attack_sound:s.Sound = s.load_sound("assets/audio/attack.wav")

def play_music():
    """Запустить фоновую музыку (если файл существует)."""
    s.audio.play_music("assets/audio/background_music.mp3", loops=-1, volume=0.3)

def stop_music():
    """Остановить фоновую музыку."""
    s.audio.stop_music()

