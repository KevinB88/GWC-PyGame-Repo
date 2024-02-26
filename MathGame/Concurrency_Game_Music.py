import threading
import pygame
import time
import subprocess


def speak(text):
    subprocess.run(['say', text])


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


speak("Hello")

music_file = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/Sound_FX/music/LoneDigger.wav'

music_thread = threading.Thread(target=play_music, args=(music_file, ))

music_thread.start()

speak("Hello")

time.sleep(1)

speak("Hello")

print("Main program is running...")


time.sleep(10)



ask = input("input some stuff: ")


print("Main program is still running..")


music_thread.join()
print("Main program ends.")

