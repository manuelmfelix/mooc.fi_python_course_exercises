# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

h = 1
x = 320
y = 240
xvelocity = 4
yvelocity = 4
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))    
    window.blit(ball, (x, y))

    pygame.display.flip()

    if x+ball.get_width() >= 640 or x <= 0:
        xvelocity = -xvelocity
    if y+ball.get_height() >= 480 or y <= 0:
        yvelocity = -yvelocity

    x += xvelocity
    y += yvelocity

    clock.tick(60)