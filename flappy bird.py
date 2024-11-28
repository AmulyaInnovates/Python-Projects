import pygame
import random

pygame.init()

# Set up the screen
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Load images
background = pygame.image.load("background.png").convert()
bird_image = pygame.image.load("bird.png").convert_alpha()
pipe_image = pygame.image.load("pipe.png").convert_alpha()

# Set up variables
bird_x = 50
bird_y = 200
bird_speed = 0
gravity = 0.25
jump_speed = -4.5
score = 0
font = pygame.font.Font(None, 36)
pipes = []
pipe_gap = 100
pipe_frequency = 100

# Functions
def add_pipe():
    pipe_x = screen_width
    pipe_y = random.randint(100, 400)
    pipes.append((pipe_x, pipe_y))

def move_pipes():
    for i, pipe in enumerate(pipes):
        pipe_x, pipe_y = pipe
        pipe_x -= 2
        pipes[i] = (pipe_x, pipe_y)
        if pipe_x < -pipe_image.get_width():
            pipes.pop(i)
            add_pipe()

def check_collision():
    global score
    for pipe in pipes:
        pipe_x, pipe_y = pipe
        if bird_x + bird_image.get_width() > pipe_x and bird_x < pipe_x + pipe_image.get_width():
            if bird_y < pipe_y or bird_y + bird_image.get_height() > pipe_y + pipe_gap:
                score = 0
                pipes.clear()
                bird_y = 200
                return True
    if bird_y < 0 or bird_y + bird_image.get_height() > screen_height:
        score = 0
        pipes.clear()
        bird_y = 200
        return True
    return False

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = jump_speed

    # Update variables
    bird_speed += gravity
    bird_y += bird_speed
    move_pipes()
    if len(pipes) > 0:
        pipe_x, pipe_y = pipes[0]
        if pipe_x < bird_x:
            score += 1
            pipes.pop(0)
            add_pipe()

    # Check for collision
    if check_collision():
        bird_speed = 0

    # Draw objects
    screen.blit(background, (0, 0))
    for pipe in pipes:
        pipe_x, pipe_y = pipe
        screen.blit(pipe_image, (pipe_x, pipe_y - pipe_image.get_height()))
        screen.blit(pygame.transform.flip(pipe_image, False, True), (pipe_x, pipe_y + pipe_gap))
    screen.blit(bird_image, (bird_x, bird_y))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

pygame.quit()
