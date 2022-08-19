# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width = 640
window_height = 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

#First robot
x1 = 0
y1 = 100
velocity1 = 1
direction1 = 1 # 1 = right, 2 = left

#Second robot 
x2 = 0
y2 = 200
velocity2 = 2
direction2 = 1 # 1 = right, 2 = left

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    #First robot movement from side to side 
    if direction1 == 1:
        x1 += velocity1
        if x1 >=  window_width - width:
            direction1 = 2
    elif direction1 == 2:
        x1 -= velocity1
        if x1 <=  0:
            direction1 = 1
    
    #First robot movement from side to side 
    if direction2 == 1:
        x2 += velocity2
        if x2 >=  window_width - width:
            direction2 = 2
    elif direction2 == 2:
        x2 -= velocity2
        if x2 <=  0:
            direction2 = 1

    clock.tick(60)