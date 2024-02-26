# import pyttsx3
#
#
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#
#
# speak("Hello, how are you today?")

import subprocess


def speak(text):
    subprocess.run(['say', text])


speak("Hello, how are you today?")