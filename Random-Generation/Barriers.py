import pygame
import random
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Default sound effects

# player_impact_sound = pygame.mixer.Sound('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/Sound-Effects/hurt_c_08-102842.mp3')
# player_move_up_sound = pygame.mixer.Sound('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/Sound-Effects/movement-swipe-whoosh-3-186577.mp3')
# player_move_down_sound = pygame.mixer.Sound('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/Sound-Effects/movement-swipe-whoosh-3-186577.mp3')
# bullet_spawn = pygame.mixer.Sound()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# FPS
FPS = 60
clock = pygame.time.Clock()


class Barrier:
    def __init__(self, width, height, speed, color=RED):
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.x = SCREEN_WIDTH + 50
        self.y = random.randint(0, SCREEN_HEIGHT - self.height)

    def move(self):
        """Move the barrier leftwards."""
        self.x -= self.speed

    def draw(self):
        """Draw the barrier on the screen."""
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.x < -self.width

    def collides_with(self, player_rect):
        barrier_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return barrier_rect.colliderect(player_rect)


class Player:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, direction):
        if direction == 'up' and self.rect.top > 0:
            self.rect.y -= self.speed
        elif direction == 'down' and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)


class PlayerShape:
    def __init__(self, color, position=(100, 100), size=(50, 50)):
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.speed = 10

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


def game_loop():
    barriers = []
    barrier_add_counter = 0
    running = True
    player_hit = False
    player_lives = 27
    player_regen_counter = 0
    player_moved = False
    player_moved_counter_up = 0
    player_moved_counter_down = 0
    player_initial_tap = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)

        # Add a new barrier every 90 frames
        barrier_add_counter += 1
        if barrier_add_counter >= 15:
            barriers.append(Barrier(width=50, height=random.randint(10, 30), speed=random.randint(10, 30)))
            barrier_add_counter = 0

        # Move and draw barriers
        for barrier in barriers[:]:
            barrier.move()
            barrier.draw()

            if barrier.off_screen():
                barriers.remove(barrier)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move('up')
            player_moved_counter_up += 1
        elif keys[pygame.K_DOWN]:
            player.move('down')
            player_moved_counter_down += 1
        elif keys[pygame.K_q]:
            running = False

        if player_moved_counter_up == 6:
            # player_move_up_sound.play()
            player_moved_counter_up = 0

        if player_moved_counter_down == 6:
            # player_move_down_sound.play()
            player_moved_counter_down = 0

        player.draw()

        for barrier in barriers:
            if barrier.collides_with(player.rect):
                # print("Game Over!")
                player.color = WHITE
                player_hit = True
                player_initial_tap = True
                player_lives -= 1
                # pygame.quit()
                # sys.exit()

        if player_hit and player_regen_counter > 10:
            player_hit = False
            player.color = player_color
            player_regen_counter = 0
        else:
            player_regen_counter += 1

        if player_initial_tap:
            # player_impact_sound.play()
            player_initial_tap = False

        if player_lives == 0:
            pygame.quit()
            sys.exit()

        print(player_lives)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":

    player_color = (0, 0, 255)
    # player = Player('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/Images/Pug-GWC-EX.jpeg',
    #                 x=100, y=SCREEN_HEIGHT // 2)
    player = PlayerShape(color=player_color, position=(100, 100), size=(50, 50))

    game_loop()
    pygame.quit()
    sys.exit()
