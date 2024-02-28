# File strictly for bot voice unit testing, and other functions

import subprocess
import json
import random


def speak(message, voice):
    subprocess.run(['say', '-v', voice, message])

# opens the JSON file in read mode, and uses json.load() to parse the file into a Python dictionary


def load_voice_lines(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def get_voice_lines_by_category(category):
    voice_lines = load_voice_lines('default_daniel_voice_lines.json')
    return voice_lines.get(category, [])


greetings = get_voice_lines_by_category('greetings')

speak(greetings[random.randint(0, len(greetings)-1)], 'Daniel')


# people = ['Albert', 'Alice', 'Alva', 'Amélie', 'Amira', 'Anna', 'Bad News', 'Bahh', 'Bells',
#           'Boing', 'Bubbles', 'Carmit', 'Cellos', 'Damayanti', 'Daniel', 'Daria', 'Wobble', 'Eddy',
#           'Ellen', 'Good News', 'Grandma', 'Jester', 'Ioana', 'Jacques', 'Joana', 'Junior', 'Kanya',
#           'Kathy', 'Kyoko', 'Lana', 'Laura', 'Lekha', 'Lesya', 'Linh', 'Luciana', 'Majed', 'Milnea',
#           'Moira', 'Mónica', 'Organ', 'Paulina', 'Superstar', 'Ralph', 'Reed', 'Rishi', 'Sara',
#           'Satu', 'Tessa', 'Thomas', 'Tingting', 'Trinoids', 'Yelda', 'Yuna', 'Zarvox', 'Zosia', 'zuzana']
#
#
# for person in people:
#     speak("Hey I am "+person+" and this is my voice! Excellent!", person)

#
# USA = """ Say, can you see
# By the dawn's early light
# What so proudly we hailed
# At the twilight's last gleaming?
# Whose broad stripes and bright stars
# Through the perilous fight
# O'er the ramparts we watched,
# Were so gallantly, yeah, streaming?
# And the rockets' red glare
# The bombs bursting in air
# Gave proof through the night
# That our flag was still there
# O say, does that star-spangled banner yet wave
# O'er the land of the free and the home of the brave"""


