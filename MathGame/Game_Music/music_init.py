
import pygame
import random


def play_music(file_path, stop_event, volume=1.0):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        if stop_event.is_set():
            pygame.mixer.music.stop()
            break


# No stop event

def play_music_no_stop_event(file_path, volume=1.0):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)



def play_track():

    music_track_1 = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/Sound_FX/music/LoneDigger.wav'
    music_track_2 = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/Sound_FX/music/Somebody That I Used To Know (2021 Remaster) [8 Bit Tribute to Gotye] - 8 Bit Universe.wav'
    music_track_3 = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/Sound_FX/music/Talking In Your Sleep (Five Nights at Freddy_s) [8 Bit Tribute to The Romantics] - 8 Bit Universe.wav'

    playlist = [music_track_1, music_track_2, music_track_3]

    random_track = playlist[random.randint(0, len(playlist)-1)]

    play_music(random_track)



