import pygame
import sys
import threading
import time
import subprocess
import math
# import pygame.mixer


def speak(voice, message):
    subprocess.run(['say', '-v', voice, message])


def object_move_rate(player_x_pos, screen_w, t):
    return (screen_w - player_x_pos) // t


def timer(secs):
    time.sleep(secs)
    speak('Daniel', 'The object has reached the player!')


pygame.init()

screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background_color = (0, 0, 0)
object_color = (255, 0, 0)

# Create a color wheel to define the colors easier:
player_color = (0, 255, 0)
player_position = [screen_width // 2, screen_height // 2]
player_size = [100, 100]
player_speed = 0

line_color = (255, 255, 255)
line_position = [player_position[0], 0]
line_size = [10, 1000]
line_speed = 0

timer_counter = 0
seconds = 7

time_thread = threading.Thread(target=timer, args=(seconds,))
speak_thread = threading.Thread(target=speak, args=('Daniel', f'This process iterated {timer_counter} times'))

object_position = [0, screen_height // 2]
object_size = [50, 50]
object_speed = 5

clock = pygame.time.Clock()

flag = 0

fixed_rate = object_move_rate(player_position[0], screen_width, seconds)

speak_flag = 0

start_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    timer_counter += 1

    delta_time = clock.tick(60) / 1000.0

    # if flag < 1:
    #     time_thread.start()
    #     flag += 1

    object_position[0] += (fixed_rate * (1/60)) * 2

    if object_position[0] >= player_position[0]:
        if speak_flag < 1:
            print(timer_counter)
            print(f'Rate: {timer_counter / seconds} increments per second.')
            current_time = time.time()
            print(f'Elapsed time: {math.floor(current_time - start_time)} seconds.')
            speak('Daniel', 'The object has reached the player!')

            speak_flag += 1

    # if object_position[0] > screen_width:
    #     object_position[0] = 0 - object_size[0]

    screen.fill(background_color)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        running = False

    pygame.draw.rect(screen, object_color, pygame.Rect(object_position[0], object_position[1], object_size[0], object_size[1]))
    pygame.draw.rect(screen, player_color, pygame.Rect(player_position[0], player_position[1], player_size[0], player_size[1]))
    pygame.draw.rect(screen, line_color, pygame.Rect(line_position[0], line_position[1], line_size[0], line_size[1]))

    pygame.display.flip()

    clock.tick(60)

# time_thread.join()

pygame.quit()
sys.exit()


