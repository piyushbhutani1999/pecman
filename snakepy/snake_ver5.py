## collisions and snake in function
import pygame
import time
import random

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
    gameDisplay.blit(screen_text, [(display_width/3)-80 , display_height/2])
    #blit function help in showing the text to screen [x and y cordinate of showing]

gameDisplay = pygame.display.set_mode((display_width,display_height))
# set the display of the game

def snake(lead_x,lead_y,block_size):
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])

    

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
    feed_x = random.randint(0, (display_width/7)+1)
    feed_x = feed_x*7
    feed_y = random.randint(0, (display_height/7)+1)
    feed_y = feed_y*7
    
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
##include feed 
        if lead_x == feed_x and lead_y ==feed_y:
            feed_x = random.randint(0, (display_width/7)+1)
            feed_x = feed_x*7
            feed_y = random.randint(0, (display_height/7)+1)
            feed_y = feed_y*7
            
        print(f"lead_x={lead_x} lead_y={lead_y}")
        gameDisplay.fill(white)
        snake(lead_x,lead_y,block_size)
        pygame.draw.rect(gameDisplay,red,[feed_x,feed_y,block_size,block_size])
        clock.tick(FPS)
        pygame.display.update()
        
    pygame.quit()
    quit()
gameLoop()
