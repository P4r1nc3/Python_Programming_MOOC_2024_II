# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width = 640
window_height = 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0,0,0))

for i in range(10):
    for j in range(10):
        window.blit(robot, (75+10*i+40*j, 100+i*20))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
