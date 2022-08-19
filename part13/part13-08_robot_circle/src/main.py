import pygame
import math
 
pygame.init()

window_width, window_height = 640, 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")
 
width = robot.get_width()
height = robot.get_height()

angle = 0
radius = 150
number = 10
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    window.fill((0, 0, 0))
    for i in range(number):
        x = window_width/2+math.cos(angle+2*math.pi*i/number)*radius-width/2
        y = window_height/2+math.sin(angle+2*math.pi*i/number)*radius-height/2
        window.blit(robot, (x, y))
    pygame.display.flip()
 
    angle += 0.01
    clock.tick(60)