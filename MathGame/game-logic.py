# This file consists of helper functions and game logic

import random
import time
import array


def space():
    print()


def star_space():
    print("**********************************************************")



    '''
        Tiers decide the difficulty/range of the values expected for the arithmetic operation

        Tier 0:         0 - 5
        Tier I:         1 - 10
        Tier II:        1 - 15
        Tier III:       5 - 25
        Tier IV:        7 - 30
        Tier V:         11 - 37
    '''


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
def arithmetic_question():

    lower_bound, upper_bound = tier_arithmetic_range(1)

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


def random_cheer():
    cheers = ["Great job!", "Excellent!", "Incredible!", "Keep it up!", "Let's Go!", "Fantastic!", "Keep pleasing!", "That's how its done!"]
    # return cheers[index % len(cheers)]
    print(cheers[random.randint(0, len(cheers)-1)])


def random_jeer():
    jeers = ["Wrong!", "Oops!", "That's not right!", "Incorrect!", "Oh come on!", "Get it right next time will you?", "Are you kidding me?", "That ain't right pal.."]
    # return jeers[index % len(jeers)]
    print(jeers[random.randint(0, len(jeers)-1)])


def random_invalid_reply():
    invalid_replies = ["Umm, what?!", "Try again pal..", "That's not a valid answer..", "What did you mean to type?!", "Uhh, try a number next time..", "Not even close.."]
    print(invalid_replies[random.randint(0, len(invalid_replies)-1)])


def after_game_report(correct, incorrect, good_streak, bad_streak, questions, accumulated):
    star_space()
    print("Your report card: ")
    print("Total number of questions: " + str(questions))
    print("Number of correct answers: " + str(correct))
    print("Longest GOOD streak: " + str(good_streak))
    print("Number of wrong answers: " + str(incorrect))
    print("Longest BAD streak: " + str(bad_streak))
    print("Your accumulated score: " + str(accumulated))
    star_space()


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

    question_count = 0

    # user_select_tier = input("Select a tier: ")

    print("If you would like to end the game immediately type in 'Q' or 'QUIT'..")
    time.sleep(1)

    print("Good luck!")
    time.sleep(1)
    space()

    while True:

        actual_answer, question = arithmetic_question()

        user_input_answer = input(question)

        if user_input_answer.lower() == 'q' or user_input_answer.lower() == 'quit':
            break

        if not user_input_answer.isdigit():
            random_invalid_reply()
            score = len(user_input_answer)
            total_score -= score

            print("-"+str(score)+" points...")
            time.sleep(3)

            if total_score < 0:
                break

        elif int(user_input_answer) == actual_answer:

            random_cheer()
            good_streak_count += 1
            correct_count += 1

            if good_streak_count > good_streak_longest:
                good_streak_longest = good_streak_count

            if good_streak_count % 3 == 0 and good_streak_multiplier < 4:
                good_streak_multiplier += 1

                if good_streak_multiplier == 4:
                    print("You've reached the maximum streak!")
                    random_cheer()
                    print("Multiplier: " + str(good_streak_multiplier))
                else:
                    print("Your on a streak!")
                    print("Multiplier: " + str(good_streak_multiplier))
                space()

                if bad_streak_count > 0:
                    print("You've redeemed yourself!")
                    print("Your BAD streak has reset to 0!")
                    random_cheer()
                    space()

                bad_streak_multiplier = 1
                bad_streak_count = 0

            score = actual_answer * good_streak_multiplier
            total_score += score
            accumulated_score += score

            print("+"+str(score)+" points!")
            line_space()

        elif int(user_input_answer) != actual_answer:
            random_jeer()

            bad_streak_count += 1
            wrong_count += 1
            good_streak_count = 0
            good_streak_multiplier = 0

            if bad_streak_count > bad_streak_longest:
                bad_streak_longest = bad_streak_count

            if bad_streak_count % 2 == 0 and bad_streak_count > 0 and bad_streak_multiplier < 4:
                bad_streak_multiplier += 1
                if bad_streak_count == 2:
                    print("You've started a BAD streak!")
                elif bad_streak_multiplier == 4:
                    print("You've reached the MAX-BAD streak multiplier!")
                else:
                    print("You're still on a BAD streak!")
                print("BAD streak multiplier: " + str(bad_streak_multiplier))
                random_jeer()

            score = actual_answer * 2 * bad_streak_multiplier
            total_score -= score

            if total_score < 0:
                break

            print("-"+str(score)+" points...")
            time.sleep(3)
            line_space()

        question_count += 1

    line_space()
    print("Game Over!")
    after_game_report(correct_count, wrong_count, good_streak_longest, bad_streak_longest, question_count, accumulated_score)


if __name__ == "__main__":
    math_game_v1()











