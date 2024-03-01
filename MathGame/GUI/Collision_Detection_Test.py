import pygame
import sys
import random
import time
import subprocess
import threading

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
background_color = (30, 30, 30)
player_color = (100, 149, 237)  # Cornflower blue
bullet_color = (255, 255, 255)  # White
target_color = (255, 69, 0)  # Red

# Player attributes
player_size = 50
player_pos = [screen_width // 2, screen_height - player_size]
player_speed = 10

# Bullet attributes
bullet_width = 5
bullet_height = 10
bullet_speed = 20
bullets = []  # List to keep track of bullets

# Target attributes
target_width, target_height = 50, 20
targets = [[random.randint(0, screen_width-target_width), random.randint(0, 100)] for _ in range(10)]

clock = pygame.time.Clock()


def speak(message):
    subprocess.run(['say', '-v', 'Daniel', message])


boom_thread = threading.Thread(target=speak, args=('Boom',))
pew_thread = threading.Thread(target=speak, args=('pew',))


def move_bullets(bullets):
    """Move bullets and remove those that are off-screen."""
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)


def draw_objects():
    """Draw player, bullets, and targets."""
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_width, bullet_height))
    for target in targets:
        pygame.draw.rect(screen, target_color, (target[0], target[1], target_width, target_height))


def detect_collision(targets, bullets):
    """Detect collisions between bullets and targets, removing any targets hit."""
    for target in targets[:]:
        for bullset in bullets[:]:
            if target[0] < bullet[0] < target[0] + target_width and target[1] < bullet[1] < target[1] + target_height:
                targets.remove(target)
                bullets.remove(bullet)
                break  # Exit this loop to avoid modifying list during iteration


ammo = 10

fire_tick = 0
fire_flag = True

start_time = time.time()
reload_flag = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ammo >= 1 and fire_flag:
                # Shoot a bullet
                bullet_x = player_pos[0] + player_size // 2 - bullet_width // 2
                bullet_y = player_pos[1]
                bullets.append([bullet_x, bullet_y])
                ammo -= 1
                fire_tick = 0
                fire_flag = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_q]:
        running = False
    if keys[pygame.K_r] and ammo == 0:
        ammo += 10
        reload_flag = False
        # Check the time since the last reload

    screen.fill(background_color)

    move_bullets(bullets)
    detect_collision(targets, bullets)
    draw_objects()

    pygame.display.flip()
    clock.tick(30)

    if fire_tick == 8:
        fire_flag = True
    else:
        fire_tick += 1

    # current_time = time.time()
    #
    # if current_time - start_time > 2 and ammo == 0:
    #     print(current_time - start_time)
    #     reload_flag = True
    #     start_time = current_time

pygame.quit()
sys.exit()
