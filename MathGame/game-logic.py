# This file consists of helper functions and game logic

# Important: replace temp music with personal-made tracks
# Important: organize code, employ modularity
# Create modules for separate tasks
# Incorporate a PyGame GUI

import random
import time
import pygame.mixer
import threading

from Text_To_Speech_Pack.Math_Game_Speech_Module import speak
from Game_Music.music_init import play_music
from GameVoiceLines import lines

pygame.mixer.init()

correct_sound_path = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/MediaPipe/Sound-Effects/131662__bertrof__game-sound-correct_v2.wav'
correct_sound = pygame.mixer.Sound(correct_sound_path)

wrong_sound_path = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/MediaPipe/Sound-Effects/131657__bertrof__game-sound-wrong.wav'
wrong_sound = pygame.mixer.Sound(wrong_sound_path)

voice = 'Daniel'
character = 'Rishi'

# Available characters: Samantha(English), Daniel(English), Thomas(French), Milena(Russian), Whisper(WARNING: Creepy), Zarox (Robotic)
# Moira (Irish English), Tessa (South African English)


def random_positive_word_str():
    positive_words = ['Cool', 'Excellent', 'Epic', 'Great', 'Nice', 'Good', 'Super', 'Rad']
    return positive_words[random.randint(0, len(positive_words)-1)]


def space():
    print()


def star_space():
    print("**********************************************************")


def line_space():
    print("----------------------------------------------------------")


# Helper function
def tier_arithmetic_range(tier):

    if tier == 0:
        return 0, 5
    elif tier == 1:
        return 1, 10
    elif tier == 2:
        return 1, 15
    elif tier == 3:
        return 5, 25
    elif tier == 4:
        return 7, 30
    elif tier == 5:
        return 11, 37
    else:
        return -1


# Generating the arithmetic question: consisting of addition & multiplication
# The difficulty argument decides the range of the numbers for the arithmetic operation
def arithmetic_question(tier):

    lower_bound, upper_bound = tier_arithmetic_range(tier)

    number_1 = random.randint(lower_bound, upper_bound)
    number_2 = random.randint(lower_bound, upper_bound)
    operator_type = random.randint(0, 1)

    if operator_type == 0:
        answer = number_1 + number_2
        operator_symbol = '+'
    else:
        answer = number_1 * number_2
        operator_symbol = '*'

    question = str(number_1) + operator_symbol + str(number_2) + " = "

    return answer, question


def random_cheer(voiced):

    # cheers = ["Great job!", "Excellent!", "Incredible!", "Keep it up!", "Let's Go!", "Fantastic!", "Keep pleasing!", "That's how its done!"]
    cheers = lines.default_voice_cheers
    # return cheers[index % len(cheers)]
    if voiced:
        speak((cheers[random.randint(0, len(cheers)-1)]), character)
    else:
        print(cheers[random.randint(0, len(cheers)-1)])


def random_jeer(voiced):
    # jeers = ["Wrong!", "Oops!", "That's not right!", "Incorrect!", "Oh come on!", "Get it right next time will you?", "Are you kidding me?", "That ain't right pal.."]
    jeers = lines.default_voice_jeers
    # return jeers[index % len(jeers)]

    if voiced:
        speak((jeers[random.randint(0, len(jeers) - 1)]), character)
    else:
        print(jeers[random.randint(0, len(jeers)-1)])


def random_invalid_reply(voiced):
    invalid_replies = ["Umm, what?!", "Try again pal..", "That's not a valid answer..", "What did you mean to type?!", "Uhh, try a number next time..", "Not even close.."]

    if voiced:
        speak(invalid_replies[random.randint(0, len(invalid_replies)-1)], character)
    else:
        print(invalid_replies[random.randint(0, len(invalid_replies)-1)])


def random_invalid_user_reply(voiced):
    invalid_user_replies = ['Could you please re-read what I asked you?', "Wh-what are you doin'?", "It ain't that hard pal, common.", "Try again, will ya'?", "Yeah that don't look right.."]

    if voiced:
        speak(invalid_user_replies[random.randint(0, len(invalid_user_replies)-1)], character)
    else:
        print(invalid_user_replies[random.randint(0, len(invalid_user_replies)-1)])


def after_game_report(correct, incorrect, good_streak, bad_streak, questions, accumulated):
    # ending_tune.play()
    star_space()
    print("Your report card: ")
    print("Total number of questions: " + str(questions))
    print("Number of correct answers: " + str(correct))
    print("Longest GOOD streak: " + str(good_streak))
    print("Number of wrong answers: " + str(incorrect))
    print("Longest BAD streak: " + str(bad_streak))
    print("Your accumulated score: " + str(accumulated))
    star_space()


def game_voice_intro(voiced):
    intro_list = lines.default_voice_game_intro
    intro = intro_list[random.randint(0, len(intro_list)-1)]
    if voiced:
        speak(intro, character)
    else:
        print(intro)


def game_voice_outro(voiced):
    outro_list = lines.default_voice_game_outro
    outro = outro_list[random.randint(0, len(outro_list)-1)]
    if voiced:
        speak(outro, character)
    else:
        print(outro)


def game_voice_rule_inquiry(voiced):
    inquiry_list = lines.default_voice_rule_inquiry
    inquiry = inquiry_list[random.randint(0, len(inquiry_list)-1)]
    if voiced:
        speak(inquiry, character)
    else:
        return inquiry


def game_voice_rule_skip(voiced):
    skip_replies = lines.default_voice_rule_skip
    reply = skip_replies[random.randint(0, len(skip_replies)-1)]
    if voiced:
        speak(reply, character)
    else:
        print(reply)


def game_voice_streak_cheer(voiced):
    streak_cheers = lines.default_voice_streak_initiated
    cheer = streak_cheers[random.randint(0, len(streak_cheers)-1)]
    if voiced:
        speak(cheer, character)
    else:
        print(cheee)

# Be warned!
def game_voice_cheers_18(voiced):
    cheers_18 = lines.default_voice_18_cheers
    cheer = cheers_18[random.randint(0, len(cheers_18)-1)]
    if voiced:
        speak(cheer, character)
    else:
        print(cheer)



def math_game_v1():

    total_score = 0
    accumulated_score = 0

    correct_count = 0
    good_streak_multiplier = 1
    good_streak_longest = 0
    good_streak_count = 0

    wrong_count = 0
    bad_streak_multiplier = 1
    bad_streak_longest = 0
    bad_streak_count = 0

    streak_message = 0

    question_count = 0

    # ending_tune.play()

    # introduction to the game function
    game_voice_intro(voice)

    time.sleep(1)

    # rule inquiry
    game_voice_rule_inquiry(voice)

    user_response = input(game_voice_rule_inquiry(False)+" ")

    while True:

        if user_response.lower() == 'yes' or user_response.lower() == 'no':
            break

        random_invalid_user_reply(True)
        time.sleep(1)
        user_response = input(game_voice_rule_inquiry(False) + ": ")

    if user_response == 'yes'.lower():

        if voice:
            speak(random_positive_word_str()+", let's check it out!", character)
        else:
            print(random_positive_word_str()+", let's check it out!")

        star_space()
        print("""
        Rules of the Game:

        1. GAMEPLAY
            a. You are given arithmetic questions. With numbers to multiply and add between 1 and 15.
            b. Maintain a score above 0 to continue playing!

        2. SCORING/POINTS
            a. For every correct answer: The answer to the question is added to your total score
            b. For every wrong answer: The actual answer to the question is multiplied by 2 and then subtracted from your total score

        3. STREAKS/BONUS POINTS
            a. Good streak:
                i. For every 3 questions correct, the answer to your question is multiplied by a number initially starting at 1.
                ii. You are able to increase your streak multiplier until 4. Which means that 16 questions correct in a row will yield a score multiplier of 4.
                iii. The result from the multiplication is multiplied by your answer and added to your total score
                iv. Your streak comes to an end upon your first incorrect answer.

            b. Bad Streak:
                i. For every 2 questions incorrect, the answer to your question is multiplied by a number initially starting at 1, on top of it being multiplied by 2
                ii. The multiple increases until a max of 4 for every 2 questions incorrect. Which means that 8 wrong answers in a row yields a multiplier of 4.
                iii. The result from the multiplication is then multiplied by 2 and the actual answer of the question.

                    EX. The maximum penalty is 8 * 2 * ACTUAL ANSWER. If the actual answer to a question is 100, then 1600 points are subtracted from your score!
                iv. You can "redeem" yourself/reset your "BAD" streak after initiating a "GOOD" streak. Otherwise, your "BAD" streak will remain!
        """)
        star_space()

    else:
        game_voice_rule_skip(voice)

    # tier confirmation
    if voice:
        speak("Awesome! Select a tier!", character)
    else:
        print("Awesome! Select a tier: ")

    print("""
    Tiers decide the difficulty/range of the values expected for the arithmetic operation

    Tier 0:         0 - 5
    Tier I:         1 - 10
    Tier II:        1 - 15
    Tier III:       5 - 25
    Tier IV:        7 - 30
    Tier V:         11 - 37
    """)

    user_select_tier = ''

    while not user_select_tier.isdigit() or int(user_select_tier) < 0 or int(user_select_tier) > 5:
        user_select_tier = input("Select a tier: ")
        if not user_select_tier.isdigit():
            # tiers: selecting a number from the provided list
            if voice:
                speak("Please select a number from the choices above...", character)
            else:
                print("Please select a number from the choices above...")
            time.sleep(1)
        elif int(user_select_tier) < 0 or int(user_select_tier) > 5:
            if voice:
                speak("Value must be between the tier ranges above...", character)
            else:
                print("Value must be between the tier ranges above...")

    # getting started
    if voice:
        speak("Great! Let's get started!", character)
    else:
        print("Great! Let's get started!")
    time.sleep(1)

    # information on ending the game
    if voice:
        speak("If you would like to end the game immediately type in 'Q' or 'QUIT'..", character)
    else:
        print("If you would like to end the game immediately type in 'Q' or 'QUIT'..", character)
    time.sleep(1)

    # wishing the player good luck
    if voice:
        speak("Good luck!", character)
    else:
        print("Good luck!")
    time.sleep(1)
    space()

    # *****
    music_track_1 = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/Sound_FX/music/LoneDigger.wav'
    music_track_2 = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/Sound_FX/music/Somebody That I Used To Know (2021 Remaster) [8 Bit Tribute to Gotye] - 8 Bit Universe.wav'
    music_track_3 = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/MathGame/Sound_FX/music/Talking In Your Sleep (Five Nights at Freddy_s) [8 Bit Tribute to The Romantics] - 8 Bit Universe.wav'

    playlist = [music_track_1, music_track_2, music_track_3]

    random_track = playlist[random.randint(0, len(playlist) - 1)]
    # *****

    # Create an  event object that can be used to signal the thread to stop
    stop_event = threading.Event()

    music_thread = threading.Thread(target=play_music, args=(random_track, stop_event, 0.2))
    music_thread.start()

    while True:

        actual_answer, question = arithmetic_question(int(user_select_tier))

        user_input_answer = input(question)

        if user_input_answer.lower() == 'q' or user_input_answer.lower() == 'quit':
            stop_event.set()
            break

        if not user_input_answer.isdigit():
            random_invalid_reply(True)
            wrong_sound.play()
            wrong_count += 1
            score = len(user_input_answer)
            total_score -= score

            print("-"+str(score)+" points...")
            # time.sleep(3)

            if total_score < 0:
                break

        elif int(user_input_answer) == actual_answer:

            correct_sound.play()
            random_cheer(True)
            good_streak_count += 1
            correct_count += 1
            streak_message += 1

            if good_streak_count > good_streak_longest:
                good_streak_longest = good_streak_count

            if good_streak_count % 3 == 0 and good_streak_multiplier < 4:
                good_streak_multiplier += 1

                if good_streak_multiplier == 4:
                    if voice:
                        speak("You've reached the maximum streak multiplier!", character)
                    else:
                        print("You've reached the maximum streak multiplier!")
                    random_cheer(True)
                    print("Multiplier: " + str(good_streak_multiplier))
                else:
                    game_voice_streak_cheer(voice)
                    print("Multiplier: " + str(good_streak_multiplier))
                space()

            if good_streak_multiplier >= 4 and streak_message % random.randint(3, 5) == 0:
                game_voice_streak_cheer(voice)

            # if good_streak_multiplier >= 4 and good_streak_multiplier < 16 and streak_message % 3 == 0:
            #     game_voice_cheers_18(voice)
            # elif good_streak_multiplier >= 16 and streak_message % 4 == 0:
            #     game_voice_cheers_18(voice)


                if bad_streak_count > 0:
                    if voice:
                        speak("You've redeemed yourself!", character)
                    else:
                        print("You've redeemed yourself!", character)

                    if voice:
                        speak("Your BAD streak has reset to 0!", character)
                    else:
                        print("Your BAD streak has reset to 0!")

                    random_cheer(True)
                    space()

                bad_streak_multiplier = 1
                bad_streak_count = 0

            score = actual_answer * good_streak_multiplier
            total_score += score
            accumulated_score += score

            print("+"+str(score)+" points!")
            print("Good streak: "+str(good_streak_count))
            line_space()

        elif int(user_input_answer) != actual_answer:
            random_jeer(True)

            # time.sleep(1)
            wrong_sound.play()

            if voice:
                speak("The actual answer was: "+str(actual_answer), character);
                print("Answer: "+str(actual_answer));
            else:
                speak("The actual answer was: "+str(actual_answer), character);


            bad_streak_count += 1
            wrong_count += 1
            good_streak_count = 0
            good_streak_multiplier = 1

            if bad_streak_count > bad_streak_longest:
                bad_streak_longest = bad_streak_count

            if bad_streak_count % 2 == 0 and bad_streak_count > 0 and bad_streak_multiplier < 4:
                bad_streak_multiplier += 1
                if bad_streak_count == 2:
                    if voice:
                        speak("You've started a BAD streak!", character)
                    else:
                        print("You've started a BAD streak!")
                elif bad_streak_multiplier == 4:
                    if voice:
                        speak("You've reached the MAX-BAD streak multiplier!", character)
                    else:
                        print("You've reached the MAX-BAD streak multiplier!")
                else:
                    if voice:
                        speak("You're still on a BAD streak!", character)
                    else:
                        print("You're still on a BAD streak!")
                print("BAD streak multiplier: " + str(bad_streak_multiplier))
                random_jeer(True)

            score = actual_answer * 2 * bad_streak_multiplier
            total_score -= score

            if total_score < 0:
                break

            print("-"+str(score)+" points...")
            line_space()

        question_count += 1
        print("###############")
        print("Total Score: "+str(total_score))
        print("###############")

    game_voice_outro(voice)
    time.sleep(1)

    # ending_tune.play()

    stop_event.set()
    music_thread.join()

    line_space()
    print("Game Over!")
    after_game_report(correct_count, wrong_count, good_streak_longest, bad_streak_longest, question_count, accumulated_score)


if __name__ == "__main__":
    math_game_v1()











