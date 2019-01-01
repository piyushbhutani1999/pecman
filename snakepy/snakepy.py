import pygame
import random
import time
width=490
height=490
screen= pygame.display.set_mode((width,height))
gameDisplay = pygame.image.load("road.jpg").convert()
dead= False
clock = pygame.time.Clock()

while dead==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)
