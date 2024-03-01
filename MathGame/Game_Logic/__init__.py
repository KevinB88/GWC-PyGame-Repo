import math
import random
import time
import re

PI_CONSTANT = math.pi

# Utilizing regular expressions to extract the first n digits from the string:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_print(a, b):
    while b != 0:
        a, b = b, a % b
        print(a)
        print(b)
    return a


def simplified_fractions():

    counter = 0

    while True:

        numerator = random.randint(0, 100)
        denominator = random.randint(1, 100)

        print(str(numerator) + "/" + str(denominator))

        divisor = gcd(numerator, denominator)

        if divisor > 1 and numerator > 0:
            numerator /= divisor
            denominator /= divisor

        print(str(numerator) + "/" + str(denominator))

        time.sleep(1)

        counter += 1
        if counter == 15:
            break


def simplify_fraction(num, dem):
    divisor = gcd(num, dem)

    if divisor > 1:
        num /= divisor
        dem /= divisor

    print(str(num) + "/"+ str(dem))


def trig_question_version1():

    question_counter = 0

    while True:

        while True:
            denominator = random.randint(1, 6)
            if denominator != 5:
                break

        scalar = random.randint(0, 3)

        if scalar == 0:
            print(0)

            print("sin(0) = "+str(math.sin(0)))
            print("cos(0) = "+str(math.cos(0)))
            print("tan(0) = "+str(math.tan(0)))

        else:
            divisor = gcd(scalar, denominator)

            if divisor > 1:
                scalar /= divisor
                denominator /= divisor

            output_piece_1 = "π" if scalar == 1 else f"{scalar}π"
            output_piece_2 = "" if denominator == 1 else f"/{denominator}"
            output = output_piece_1 + output_piece_2
            print(output)

            sin_ratio = math.sin((scalar * PI_CONSTANT) / denominator)
            cos_ratio = math.cos((scalar * PI_CONSTANT) / denominator)
            tan_ratio = math.tan((scalar * PI_CONSTANT) / denominator)

            print(f"sin({output}) = "+str(sin_ratio))
            print(f"cos({output}) = "+str(cos_ratio))
            print(f"tan({output}) = "+str(tan_ratio))

        question_counter += 1

        if question_counter == 15:
            break
        else:
            time.sleep(1)

# This functions returns a question and an answer


def trig_question_version2():
    while True:
        denominator = random.randint(1, 6)
        if denominator != 5:
            break

    scalar = random.randint(0, 3)

    if scalar == 0:

        trig_dictionary = {"sin(0)": 0, "cos(0)": 1, "tan(0)": 0}

        corresponding_question = random.choice(list(trig_dictionary.keys()))
        corresponding_answer = trig_dictionary[corresponding_question]

        return corresponding_question, corresponding_answer

    else:
        divisor = gcd(scalar, denominator)

        if divisor > 1:
            scalar /= divisor
            denominator /= divisor

        output_piece_1 = "π" if scalar == 1 else f"{scalar}π"
        output_piece_2 = "" if denominator == 1 else f"/{denominator}"
        output_radians = output_piece_1 + output_piece_2

        sin_ratio = math.sin((scalar * PI_CONSTANT) / denominator)
        cos_ratio = math.cos((scalar * PI_CONSTANT) / denominator)
        tan_ratio = math.tan((scalar * PI_CONSTANT) / denominator)

        trig_dictionary = {f"sin({output_radians})": sin_ratio, f"cos({output_radians})": cos_ratio,
                           f"tan({output_radians})": tan_ratio}

        corresponding_question = random.choice(list(trig_dictionary.keys()))
        corresponding_answer = trig_dictionary[corresponding_question]

        return corresponding_question, corresponding_answer


if __name__ == "__main__":

    question_string, actual_answer = trig_question_version2()

    # Testing the random generation of trig questions for the user:

    print("Question: " + question_string)
    print("Actual answer: " + str(actual_answer))

    # Parse the user-input and use it within an actual operation for math

    # str1 = str(math.sin(PI_CONSTANT/4))
    # str2 = str(math.sqrt(2)/2)
    #
    # value_1 = read_float_first_n_digits(str1, 6)
    # value_2 = read_float_first_n_digits(str2, 6)
    #
    # if value_1 == value_2:
    #     print("They are equal!")
    # else:
    #     print("They are not equal!")
    #
    # print(str(math.sin(PI_CONSTANT/4)) + " = " + str(math.sqrt(2)/2))
    # print(str(math.sin(PI_CONSTANT/2)) + " = " + str(math.sqrt(1)/1))
    # print(str(math.sin(PI_CONSTANT/3)) + " = " + str(math.sqrt(3)/2))

    # simplify_fraction(80, 25)
    # simplified_fractions()


