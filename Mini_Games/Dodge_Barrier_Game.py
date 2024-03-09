import pygame
import sys
import random

pygame.init()

infoObject = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

SCREEN_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 255, 255)
OBSTACLE_COLOR = (255, 0, 0)
FONT_COLOR = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()

player_size = (SCREEN_WIDTH // 20, SCREEN_HEIGHT // 20)
player_speed = SCREEN_WIDTH // 100
barrier_width = SCREEN_WIDTH // 25
barrier_height = SCREEN_HEIGHT // 8
barrier_speed = SCREEN_WIDTH // 100


class Barrier:

  def __init__(self,
               width=barrier_width,
               height=barrier_height,
               speed=barrier_speed,
               color=OBSTACLE_COLOR):
    self.width = width
    self.height = height
    self.speed = speed * 2
    self.color = color

    self.x = SCREEN_WIDTH + 50
    self.y = random.randint(0, SCREEN_HEIGHT - self.height)

  def move(self):
    self.x -= self.speed

  def draw(self):
    pygame.draw.rect(screen, self.color,
                     pygame.Rect(self.x, self.y, self.width, self.height))

  def off_screen(self):
    return self.x < -self.width

  def collides_with(self, player_rect):
    barrier_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    return barrier_rect.colliderect(player_rect)


class Player:

  def __init__(self, color, position=(100, 100), size=player_size, lives=15):
    self.color = color
    self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
    self.speed = player_speed * 5
    self.lives = lives

  def draw(self):
    pygame.draw.rect(screen, self.color, self.rect)

  def move(self, direction):
    if direction == 'up' and self.rect.top > 0:
      self.rect.y -= self.speed
    elif direction == 'down' and self.rect.bottom < SCREEN_HEIGHT:
      self.rect.y += self.speed
    elif direction == 'left' and self.rect.left > 0:
      self.rect.x -= self.speed
    elif direction == 'right' and self.rect.right < SCREEN_WIDTH:
      self.rect.x += self.speed


running = True


def game_loop():
  global running
  frame_counter = 0
  barrier_spawn_rate = 30
  font = pygame.font.SysFont(None, 36)

  impact_flag = False
  impact_flag_timer = 0

  player = Player(
      color=PLAYER_COLOR)  # Assuming you have a color defined as BLUE
  barriers = [Barrier(width=20, height=60, speed=5,
                      color=OBSTACLE_COLOR)]  # Example list of barriers

  while running:

    frame_counter += 1

    if frame_counter % barrier_spawn_rate == 0:
      barriers.append(Barrier())

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      keys = pygame.key.get_pressed()

      if keys[pygame.K_UP]:
        player.move('up')
      elif keys[pygame.K_LEFT]:
        player.move('left')
      elif keys[pygame.K_RIGHT]:
        player.move('right')
      elif keys[pygame.K_DOWN]:
        player.move('down')
      elif keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

    screen.fill(
        (0, 0, 0))  # Clear the screen (assuming you have a variable `screen`)

    for barrier in barriers[:]:
      if barrier.collides_with(player.rect) and not impact_flag:
        player.lives -= 1  # Reduce player's lives by one
        impact_flag = True
        player.color = (255, 192, 103)
        if player.lives == 0:
          game_over_text = font.render('Game Over', True, FONT_COLOR)
          screen.blit(game_over_text,
                      (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                       SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
          pygame.display.flip()
          pygame.time.delay(2000)
          running = False
        break  # Exit the loop to avoid multiple collisions at once

      if barrier.off_screen():
        barriers.remove(barrier)

      barrier.move()
      barrier.draw()

    if impact_flag:
      impact_flag_timer += 1
      if impact_flag_timer >= 75:
        impact_flag_timer = 0
        impact_flag = not impact_flag
        player.color = PLAYER_COLOR

    player.draw()

    lives_text = font.render(f'Lives: {player.lives}', True, FONT_COLOR)
    # counter_text = font.render(f'Impact timer {impact_flag_timer}', True, FONT_COLOR)
    screen.blit(lives_text, (10, 10))
    # screen.blit(counter_text, (50, 100))

    pygame.display.flip()  # Update the screen
    clock.tick(FPS)


if __name__ == "__main__":
  game_loop()
