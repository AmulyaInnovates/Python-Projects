import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the player image
player_image = pygame.image.load("player.png")
player_width = 50
player_height = 100
player_image = pygame.transform.scale(player_image, (player_width, player_height))
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height
player_speed = 5
player_jump_speed = 10
player_is_jumping = False
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the game loop
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_is_jumping:
                player_is_jumping = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < screen_width - player_width:
        player_x += player_speed
    if player_is_jumping:
        player_y -= player_jump_speed
        player_jump_speed -= 1
        if player_jump_speed < -10:
            player_is_jumping = False
            player_jump_speed = 10

    # Update the player rectangle
    player_rect.x = player_x
    player_rect.y = player_y

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(player_image, player_rect)
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit pygame
pygame.quit()
