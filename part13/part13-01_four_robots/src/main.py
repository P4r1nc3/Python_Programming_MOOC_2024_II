import pygame

pygame.init()
width_window = 640
height_window = 480

window = pygame.display.set_mode((width_window, height_window))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0,0,0))

window.blit(robot, (0,0))
window.blit(robot, (width_window-width,0))
window.blit(robot, (0,height_window-height))
window.blit(robot, (width_window-width,height_window-height))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()