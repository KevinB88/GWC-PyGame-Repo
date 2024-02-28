import threading
import time


def input_with_timeout(prompt, timeout):
    print(prompt)
    result = [None]

    def wait_for_input():
        result[0] = input()

    thread = threading.Thread(target=wait_for_input())
    thread.start()

    thread.join(timeout)
    if thread.is_alive():
        print("Time is up! You didn't respond in time!")
    thread.join()
    return result[0]


user_input = input_with_timeout("Enter something within 10 seconds: ", 10)
if user_input is not None:
    print(f"You entered: {user_input}")
else:
    print("No input was provided!")
