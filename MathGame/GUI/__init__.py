import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
background_color = (30, 30, 30)
text_color = (255, 255, 255)
box_color = (60, 60, 60)

# Font setup
font = pygame.font.Font(None, 32)

# Text input box setup
input_box = pygame.Rect(100, 100, 140, 32)
text = ''
active = False  # State of the input box

# Object details
object_position = [0, screen_height // 2]
object_size = [50, 50]
object_speed = 5  # Default speed

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    try:
                        object_speed = float(text)
                    except ValueError:
                        print("Please enter a valid number.")
                    text = ''  # Reset text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Move the object
    object_position[0] += object_speed
    if object_position[0] > screen_width:
        object_position[0] = 0 - object_size[0]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    # Render
    screen.fill(background_color)
    # Draw the object
    pygame.draw.rect(screen, text_color, pygame.Rect(object_position[0], object_position[1], object_size[0], object_size[1]))
    # Draw the input box
    txt_surface = font.render(text, True, text_color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, box_color, input_box, 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
