import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Define colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Load images
car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (80, 160))
obstacle_img = pygame.image.load("obstacle.png")
obstacle_img = pygame.transform.scale(obstacle_img, (80, 80))

# Set up the car
car_width = 80
car_height = 160
car_x = (WIDTH - car_width) // 2
car_y = HEIGHT - car_height - 10
car_speed = 5

# Set up the obstacle
obstacle_width = 80
obstacle_height = 80
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

def display_score():
    score_text = font.render("Score: " + str(score), True, RED)
    window.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over!", True, RED)
    window.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    pygame.display.update()
    pygame.time.delay(2000)

# Load and play the background music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    window.fill(YELLOW)  # Yellow background color

    # Move the obstacle
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        score += 1

    # Check collision
    if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x and car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y:
        game_over()
        score = 0
        car_x = (WIDTH - car_width) // 2

    # Draw car and obstacle
    window.blit(car_img, (car_x, car_y))
    window.blit(obstacle_img, (obstacle_x, obstacle_y))

    display_score()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

