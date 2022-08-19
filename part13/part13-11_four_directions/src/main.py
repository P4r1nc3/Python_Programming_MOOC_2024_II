# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width, window_height = 640, 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

x = 0
y = 480-robot.get_height()

to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_UP:
                to_up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_UP:
                to_up = False

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        x += 5
    if to_left:
        x -= 5
    if to_down:
        y += 5
    if to_up:
        y -= 5

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)