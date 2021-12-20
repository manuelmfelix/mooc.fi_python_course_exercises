# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()
x2 = 600
y2 = 480-robot.get_height()

to_right = False
to_left = False
to_up = False
to_down = False

to_d = False
to_a = False
to_w = False
to_s = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_a:
                to_a = True
            if event.key == pygame.K_d:
                to_d = True
            if event.key == pygame.K_s:
                to_s = True
            if event.key == pygame.K_w:
                to_w = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_a:
                to_a = False
            if event.key == pygame.K_d:
                to_d = False
            if event.key == pygame.K_s:
                to_s = False
            if event.key == pygame.K_w:
                to_w = False

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        if x+robot.get_width() < 640:
            x += 2
    if to_left:
        if x > 0:
            x -= 2
    if to_down:
        if y+robot.get_height() < 480:
            y += 2
    if to_up:
        if y > 0:
            y -= 2

    if to_d:
        if x2+robot.get_width() < 640:
            x2 += 2
    if to_a:
        if x2 > 0:
            x2 -= 2
    if to_s:
        if y2+robot.get_height() < 480:
            y2 += 2
    if to_w:
        if y2 > 0:
            y2 -= 2
            

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)