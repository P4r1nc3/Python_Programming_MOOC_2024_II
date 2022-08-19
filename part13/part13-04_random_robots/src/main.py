# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame

pygame.init()

window_width = 640
window_height = 480

window = pygame.display.set_mode((window_width , window_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))

for i in range(1000):
    x = randint(0, window_width-width)
    y = randint(0, window_height-height)
    window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()