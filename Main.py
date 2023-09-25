import pygame
import random


# Screen display config
pygame.init()
pygame.display.set_caption("Snake Game")
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


# Snake parameters
square_size = 20
game_speed = 15


def generate_food():
    x_food = round(random.randrange(0, width - square_size) / float(square_size)) * float(square_size)
    y_food = round(random.randrange(0, height - square_size) / float(square_size)) * float(square_size)
    return x_food, y_food 


def draw_food(size, x_food, y_food):
    pygame.draw.rect(screen, green, [x_food, y_food, size, size])


def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], size, size])


def draw_points(points):
    font = pygame.font.SysFont("Helvetica", 35)
    text = font.render(f"Points: {points}", True, red)
    screen.blit(text, [1, 1])


def speed_select(key):

    if key == pygame.K_DOWN:
        x_speed = 0
        y_speed = square_size

    elif key == pygame.K_UP:
        x_speed = 0
        y_speed = -square_size
    
    elif key == pygame.K_RIGHT:
        x_speed = square_size
        y_speed = 0

    elif key == pygame.K_LEFT:
        x_speed = -square_size
        y_speed = 0

    return x_speed, y_speed


# Game looping
def game_running():

    fim_jogo = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_size = 1
    pixels = []

    x_food, y_food = generate_food()

    while not fim_jogo:
        screen.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True
            elif event.type == pygame.KEYDOWN:
                x_speed, y_speed = speed_select(event.key)

        draw_food(square_size, x_food, y_food)

        x += x_speed
        y += y_speed

        if x < 0 or x >= width or y < 0 or y >= height:
            fim_jogo = True

        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels[0]
        
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        draw_snake(square_size, pixels)
        draw_points(snake_size - 1)

        pygame.display.update()

        if x == x_food and y == y_food:
            snake_size += 1
            x_food, y_food = generate_food()

        clock.tick(game_speed)


game_running()

