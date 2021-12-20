# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
h = 1
v = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if h == 1 and v == 0:
        x += velocity
        y = 0
    elif h == 0 and v == 1:
        x = 640-robot.get_width()
        y += velocity
    elif h == -1 and v == 0:
        x += -velocity
        y = 480-robot.get_height()
    elif h == 0 and v == -1:
        x = 0
        y += -velocity
    
    if h == 1 and v == 0 and x+robot.get_width() >= 640:
        h = 0
        v = 1
    if h == 0 and v == 1 and y+robot.get_height() >= 480:
        h = -1
        v = 0
    if h == -1 and v == 0 and x <= 0:
        h = 0
        v = -1
    if h == 0 and v == -1 and y <= 0:
        h = 1
        v = 0
    
    clock.tick(60)