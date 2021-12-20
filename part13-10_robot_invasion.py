# WRITE YOUR SOLUTION HERE:
import pygame
from random import *

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

class robo:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y
        self.inix = x
        self.iniy = y
        if random() < 0.5:
            self.xi = 2
        else:
            self.xi = -2
        self.yi = 2
    
    def down(self):
        self.y += self.yi

    def left_right(self):
        self.x += self.xi

    def __str__(self):
        return f"robot x: {self.x}, y: {self.y}"

clock = pygame.time.Clock()

robot_army = [robo(randint(0,640),-randint(0,10000)) for a in range(0,20)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for a in robot_army:
        if a.y+robot.get_height() < 480:
            a.down()
        else:
            a.left_right()
        if a.x+robot.get_width() >= 640 or a.x <= 0:
            a.x = a.inix
            a.y = a.iniy
        window.blit(robot, (a.x,a.y))

    pygame.display.flip()

    clock.tick(60)