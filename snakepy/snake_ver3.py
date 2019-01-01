#this is about adding boundaries and movement in x and y axis

import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0 )

gameDisplay = pygame.display.set_mode((800,600))
# set the display of the game

pygame.display.set_caption("Feed The Snake")
# set the caption of the game

clock = pygame.time.Clock()
# return us a pygame clock object

gameExit = False

lead_x = 400
lead_y = 300
lead_x_change = 0
lead_y_change = 0

while not gameExit:

    for event in pygame.event.get():
##        lead_x_change = 0
##        lead_y_change = 0
##        this for loop always functions wheather there is an event or not  
##        print(event)
        if event.type == pygame.QUIT:
           gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0
        

    lead_x = lead_x + lead_x_change
    lead_y = lead_y + lead_y_change
    if lead_x > 800 or lead_x<0 or lead_y > 600 or lead_y<0:
        gameExit = True
    print(f"lead_x={lead_x} lead_y={lead_y}")
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])
    clock.tick(30)
    pygame.display.update()
    #print(f"lead_x= {lead_x} and {event}")

pygame.quit()
quit()
