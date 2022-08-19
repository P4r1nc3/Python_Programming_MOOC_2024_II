# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width, window_height = 640, 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

robot_x = 0
robot_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            robot_x = event.pos[0]-width/2
            robot_y = event.pos[1]-height/2
            
        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)