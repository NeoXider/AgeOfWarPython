import spritePro as s

attack_sound:s.Sound = s.load_sound("assets/audio/attack.wav")

def play_music():
    s.audio.play_music("assets/audio/background_music.mp3", loops=-1, volume=0.3)

def stop_music():
    s.audio.stop_music()

