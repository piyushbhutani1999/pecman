# here we include text to game and then ask ques for play again

import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0 )

display_width = 490
display_height = 490
block_size = 7
FPS = 30
##  gives message to screen
font = pygame.font.SysFont(None, 25)
## SysFont is a font type and 25 is the sixe of the font
def message(msg,color):
    screen_text = font.render(msg , True , color)
    gameDisplay.blit(screen_text, [display_width/3 , display_height/2])
    #blit function help in showing the text to screen [x and y cordinate of showing]

gameDisplay = pygame.display.set_mode((display_width,display_height))
# set the display of the game

pygame.display.set_caption("Feed The Snake")
# set the caption of the game

clock = pygame.time.Clock()
# return us a pygame clock object

def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    print("game loop")
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message("Press A to -PLAY AGAIN- and X to -QUIT-",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        gameLoop()
                    elif event.key == pygame.K_x:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
            

        lead_x = lead_x + lead_x_change
        lead_y = lead_y + lead_y_change
        if lead_x > display_width or lead_x<0 or lead_y > display_height or lead_y<0:
            gameOver = True
            
        print(f"lead_x={lead_x} lead_y={lead_y}")
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
        clock.tick(FPS)
        pygame.display.update()
        
    pygame.quit()
    quit()
gameLoop()
