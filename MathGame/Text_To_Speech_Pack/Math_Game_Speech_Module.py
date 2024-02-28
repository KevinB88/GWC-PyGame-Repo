import subprocess


def speak(text, voice):
    subprocess.run(['say', '-v', voice, text])

