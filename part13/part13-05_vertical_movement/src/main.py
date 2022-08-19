# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width = 640
window_height = 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += velocity
    if velocity > 0 and y+robot.get_height() >= 480:
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = -velocity

    clock.tick(60)