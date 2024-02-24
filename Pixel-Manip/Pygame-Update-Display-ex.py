import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

running = True

# Example rectangle: assigned with the values: 300, 220, 50, 50
sprite_rect = pygame.Rect(300, 220, 50, 50)

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        running = False

    sprite_rect.x += 1
    if sprite_rect.x > screen.get_width():
        sprite_rect.x = 0

    screen.fill((0, 0, 0))

    # Drawing something at the rectangle's position
    pygame.draw.rect(screen, (255, 0, 0), sprite_rect)

    pygame.display.update(sprite_rect)

    clock.tick(60)

pygame.quit()