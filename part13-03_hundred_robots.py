# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width_window = 640
height_window = 480
window = pygame.display.set_mode((width_window,height_window))

robot = pygame.image.load("robot.png")

width = robot.get_width()-10
window.fill((0,0,0))
for b in range(0,10):
    for a in range(0,10):
        window.blit(robot,(75+(width/3)*b+width*a,100+20*b))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()