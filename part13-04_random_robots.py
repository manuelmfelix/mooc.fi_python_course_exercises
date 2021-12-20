# WRITE YOUR SOLUTION HERE:
import pygame
from random import *

pygame.init()
width_window = 640
height_window = 480
window = pygame.display.set_mode((width_window,height_window))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()
window.fill((0,0,0))
for a in range(1,1001):
    widthR = randint(0,width_window-width)
    heightR = randint(0,height_window-height)
    window.blit(robot,(widthR,heightR))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()