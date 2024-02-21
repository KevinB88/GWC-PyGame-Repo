import pygame
import sys


class Player:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, dx=0, dy=0):
        self.rect.x += dy * self.speed
        self.rect.y += dy * self.speed


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        x = min(0, y)
        y = min(0, y)
        x = max(-(self.width - screen_width), x)
        y = max(-(self.height - screen_height), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Camera follow system")

BLACK = (0, 0, 0)

player = Player(50, 50, '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/Images/Pug-GWC-EX.jpeg')

game_world_width = 2000
game_world_height = 1500
camera = Camera(game_world_width, game_world_height)

running = True
clock = pygame.time.Clock()
fps = 60

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    dx, dy = 0, 0

    if keys[pygame.K_a]:
        dx = -1
    if keys[pygame.K_d]:
        dx = 1
    if keys[pygame.K_w]:
        dy = -1
    if keys[pygame.K_s]:
        dy = 1
    player.move(dx, dy)

    camera.update(player)

    screen.fill(BLACK)
    screen.blit(player.image, camera.apply(player))
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
sys.exit()

