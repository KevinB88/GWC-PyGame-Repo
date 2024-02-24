import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()  # Clock instance for managing frame rate
running = True
radius = 40

colors = ["Blue", "Yellow", "Red", "Black", "Orange", "Silver", "Brown"]

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

color = "Black"
background = "White"

while running:
  dt = clock.tick(60) / 1000.0

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background)
  pygame.draw.circle(screen, color, player_pos, radius)

  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    player_pos.y -= 300 * dt
  if keys[pygame.K_s]:
    player_pos.y += 300 * dt
  if keys[pygame.K_d]:
    player_pos.x += 300 * dt
  if keys[pygame.K_a]:
    player_pos.x -= 300 * dt
  if keys[pygame.K_c]:
    color = random.choice(colors)
  if keys[pygame.K_e]:
    background = random.choice(colors)

  pygame.display.flip()
