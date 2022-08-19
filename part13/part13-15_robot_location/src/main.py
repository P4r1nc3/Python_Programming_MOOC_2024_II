# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame

pygame.init()

window_width, window_height = 640, 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x = event.pos[0]
            target_y = event.pos[1]

            if target_x > robot_x and target_x < robot_x+robot.get_width() and target_y > robot_y and target_x < robot_x+robot.get_width():
                robot_x = randint(0,640-robot.get_width())
                robot_y = randint(0,480-robot.get_height())

        window.fill((0, 0, 0))
        window.blit(robot, (robot_x, robot_y))
        pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()