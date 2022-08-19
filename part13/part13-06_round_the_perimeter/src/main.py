# # WRITE YOUR SOLUTION HERE:
from turtle import width
import pygame

pygame.init()

window_width = 240
window_height = 160

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

x = 0
y = 0
velocity = 1
direction = 1 # direction 1 = right, 2 = down, 3 = left, 4 = up

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()


    if direction == 1:                               
        x += velocity
        if x + width == window_width:    
            direction = 2                              
    elif direction == 2:                               
        y += velocity
        if y + height == window_height:
            direction = 3                              
    elif direction == 3:                              
        x -= velocity
        if x == 0:                                 
            direction = 4
    elif direction == 4:                               
        y -= velocity
        if y == 0:                               
            direction = 1

    clock.tick(60)