import pygame
import sys

pygame.init()

# Establish the dimensions of the screen
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

# Optional: adding a caption to the display

pygame.display.set_caption("Moving pixel animation")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

x_pos = 0

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        running = False

    if x_pos < screen_width:
        pixels = pygame.PixelArray(screen)
        # Create a PixelArray object from the screen surface
        # Directly modify pixels on screen: each pixel accessed via (x,y) positions
        pixels[x_pos][300] = WHITE
        pixels[x_pos][301] = WHITE
        pixels[x_pos][302] = WHITE
        pixels[x_pos][303] = WHITE
        pixels[x_pos][304] = WHITE
        del pixels
    else:
        x_pos = 0

    pygame.display.flip()
    x_pos += 1
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()


