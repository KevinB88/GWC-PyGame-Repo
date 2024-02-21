import pygame
import sys

pygame.init()

window_size = (1920, 1080)
screen = pygame.display.set_mode(window_size)
'''
    screen = pygame.display.set_mode(window_size)
'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

fps = 60
clock = pygame.time.Clock()


# class Player:
#     def __init__(self, x, y, width, height, color):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.color = color
#         self.speed_y = 0
#         self.speed_x = 5
#         self.gravity = 0.5
#         self.jump_speed = -10
#         self.grounded = False
#
#     def update(self):
#         self.speed_y += self.gravity
#         self.y += self.speed_y
#
#         if self.y > window_size[1] - self.height:
#             self.y = window_size[1] - self.height
#             self.speed_y = 0
#             self.grounded = True
#
#     def draw(self, surface):
#         pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
#
#     def move_left(self):
#         self.x -= self.speed_x
#
#     def move_right(self):
#         self.x += self.speed_x
#
#     def jump(self):
#         if self.grounded:
#             self.speed_y += self.jump_speed
#             self.grounded = False


# player = Player(50,50,50,50, WHITE)

class Player:
    def __init__(self, x, y, image_path, width, height):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_y = 0
        self.speed_x = 0
        self.gravity = 0.5
        self.jump_speed = -10
        self.grounded = False

    def apply_gravity(self):
        self.speed_y += self.gravity
        self.rect.y += self.speed_y

        # Checking for collisions:

        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.grounded = True
            self.speed_y = 0

    def jump(self):
        if self.grounded:
            self.speed_y = self.jump_speed
            self.grounded = False

    def move_horizontal(self, direction):
        self.rect.x += self.speed_x * direction

    def update(self):
        self.apply_gravity()

    def check_collision(self, sprites):
        for sprite in sprites:
            if self.rect.colliderect(sprite.rect):
                pass


player_image_path = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/Images/Pug-GWC-EX.jpeg'
player = Player(500, 500, player_image_path, 500, 500)

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.move_horizontal(-1)
    if keys[pygame.K_d]:
        player.move_horizontal(1)
    if keys[pygame.K_SPACE]:
        player.jump()
    if keys[pygame.K_q]:
        running = False

    player.update()

    screen.fill(BLACK)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

    clock.tick()

pygame.quit()
sys.exit()

