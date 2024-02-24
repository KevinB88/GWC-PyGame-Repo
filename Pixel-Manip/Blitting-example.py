import pygame
import sys

pygame.init()

surface_width = 1920
surface_height = 1080

screen = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption("Blitting example")

image = pygame.image.load('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/GWC/PyGame/GWC-PyGame-Repo/Images/pug-8515766_640.png')

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Param: The image, and its destination/initial location on the surface
    screen.blit(image, (100, 100))

    pygame.display.flip()
    # Function:

pygame.quit()
sys.exit()

