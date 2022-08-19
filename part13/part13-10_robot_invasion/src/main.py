# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
# number of robots (the same robots are reused)
number = 20
 
robots = []
for i in range(number):
    # causes the new random start position to be drawn immediately
    robots.append([-1000,height])
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    for i in range(number):
        if robots[i][1]+robot.get_height() < height:
            # the robot falls downwards
            robots[i][1] += 1
        else:
            if robots[i][0] < -robot.get_width() or robots[i][0] > width:
                # new random start point
                robots[i][0] = randint(0,width-robot.get_width())
                robots[i][1] = -randint(100,1000)
            elif robots[i][0]+robot.get_width()/2 < width/2:
                # the robot moves to the left
                robots[i][0] -= 1
            else:
                # the robot moves to the right
                robots[i][0] += 1
 
    screen.fill((0, 0, 0))
    for i in range(number):
        screen.blit(robot, (robots[i][0], robots[i][1]))
    pygame.display.flip()
 
    clock.tick(60)