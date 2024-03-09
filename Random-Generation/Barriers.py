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


running = True

def game_loop():

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()






if __name__ == "__main__":

    player_color = (0, 0, 255)
    # player = Player('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/Images/Pug-GWC-EX.jpeg',
    #                 x=100, y=SCREEN_HEIGHT // 2)
    player = PlayerShape(color=player_color, position=(100, 100), size=(50, 50))

    game_loop()
    pygame.quit()
    sys.exit()
