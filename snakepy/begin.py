import pygame
import time
import random
black=(0,0,0)
width = 480
height = 480
gameDisplay = pygame.display.set_mode((width,height))
#sets our screen siur screen size
pygame.display.set_caption("Feed The Snake")
#sets screen caption on top
run = True
while run:
    gameDisplay.fill((255,255,255))
    for event in pygame.event.get():
        print(event)
    #it gives information about each and every event either the mouse move or key click
    #you can check this by print (event)
        if event.type==pygame.QUIT:
            #pygame.Quit is the cross ton the top right which quits the game
            run=False
            break
    pygame.draw.rect(gameDisplay,black,[240,240,10,10])
    # also we can use gameDisplay.fill(black,rect=[x,y,width,height])
    #help in drawing the rect. [x,y,width,height]
    pygame.display.update()
pygame.quit()
quit()
