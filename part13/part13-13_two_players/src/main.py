# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width, window_height = 640, 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png") 

width = robot.get_width()
height = robot.get_height()

#FIRST ROBOT
x1 = window_width-width
y1 = 0

#SECOND ROBOT
x2 = 0
y2 = 0

velocity = 3

#FIRST ROBOT
to_right1 = False
to_left1 = False
to_up1 = False
to_down1 = False

#SECOND ROBOT
to_right2 = False
to_left2 = False
to_up2 = False
to_down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #FIRST ROBOT
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_UP:
                to_up1 = True
            if event.key == pygame.K_DOWN:
                to_down1 = True

            #SECOND ROBOT
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_w:
                to_up2 = True
            if event.key == pygame.K_s:
                to_down2 = True      

        if event.type == pygame.KEYUP:
            #FIRST ROBOT
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_UP:
                to_up1 = False
            if event.key == pygame.K_DOWN:
                to_down1 = False

            #SECOND ROBOT
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_w:
                to_up2 = False
            if event.key == pygame.K_s:
                to_down2 = False

        if event.type == pygame.QUIT:
            exit()

    #FIRST ROBOT
    if to_right1:
        if x1 < window_width - width:
            x1 += velocity
    if to_left1:
        if x1 > 0:
            x1 -= velocity
    if to_up1:
        if y1 > 0:
            y1 -= velocity
    if to_down1:
        if y1 < window_height - height:
            y1 += velocity

    #SECOND ROBOT
    if to_right2:
        if x2 < window_width - width:
            x2 += velocity
    if to_left2:
        if x2 > 0:
            x2 -= velocity
    if to_up2:
        if y2 > 0:
            y2 -= velocity
    if to_down2:
        if y2 < window_height - height:
            y2 += velocity

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
