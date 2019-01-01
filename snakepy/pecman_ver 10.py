#snake head function and multifunctions related to snake length
import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0 )
green = (0,0,255)
display_width = 500
display_height = 500
block_size = 20
FPS = 10
head_up = pygame.image.load("snakeHeadup.fw.png")
head_down = pygame.image.load("snakeHeaddown.fw.png")
head_right = pygame.image.load("snakeHeadright.fw.png")
head_left = pygame.image.load("snakeHeadleft.fw.png")
tail = pygame.image.load("tailUp.fw.png")
head_up = pygame.image.load("snakeHeadup.fw.png")
body = pygame.image.load("body_snake.fw.png")
snakeHeadShut= pygame.image.load("snakeHeadShut.fw.png")
fruitSmall=  pygame.image.load("fruitSmall.fw.png")
fruitLarge=  pygame.image.load("fruitLarge.fw.png")
starBackground =pygame.image.load("starBackground.fw.png")
pauseWindow =pygame.image.load("pauseWindow.fw.png")
gameOverWindow = pygame.image.load("gameOverfinal.fw.png")
gameOverWindowenlarge= pygame.image.load("gameOverfinalenlarge.fw.png")
foreground = pygame.image.load("foreground.fw.png")
foregroundEnlarge=pygame.image.load("foregroundEnlarge.fw.png")
cross = pygame.image.load("cross.fw.png")
##########################################


def text_objects(text,color,size):
    smallFont = pygame.font.SysFont("comicsansms",20)
    mediumFont = pygame.font.SysFont("comicsansms",40)
    largeFont = pygame.font.SysFont("comicsansms",60)
    if size == "small":
        textsurface = smallFont.render(text,True, color)
    elif size == "medium":
        textsurface = mediumFont.render(text,True, color)
    elif size == "large":
        textsurface = largeFont.render(text,True, color)
    return textsurface,textsurface.get_rect()



def message(msg, color,y_displacement=0, size = "small", x_displacement=0):
    textsurf, textrect=text_objects(msg,color,size)
    textrect.center= (display_width/2)-x_displacement, (display_height/2)-y_displacement
    gameDisplay.blit(textsurf,textrect)

    

def pause():

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
##        gameDisplay.fill(green)
##        message("PAUSED", black, -200,size = "medium")
##        message("Press SPACE to continue or Q to quit",red,100,size = "small")
        gameDisplay.blit(pauseWindow,(0,0))
        message("PAUSED", black, -200,size = "medium")
        pygame.display.update()
        


##########################################

gameDisplay = pygame.display.set_mode((display_width,display_height))
# set the display of the game

def snake(block_size,snakeList,snakeHead,direction,check):
    
    if direction == "down":
        head = head_down
    elif direction == "up":
        head = head_up
    elif direction == "right":
        head = head_right
    elif direction == "left":
        head = head_left
    for x in snakeList:
        if x == snakeHead:
            if check==1:
                gameDisplay.blit(head,(x[0],x[1]))
            else :
                gameDisplay.blit(snakeHeadShut,(x[0],x[1]))
        else:
            gameDisplay.blit(body,(x[0],x[1]))
pygame.display.set_caption("Feed The Snake")
# set the caption of the game

clock = pygame.time.Clock()
# return us a pygame clock object

def gameLoop():
    gameExit = False
    gameOver = False
    temp=0
    snakeLength = 3
    direction = "right"
    lead_x = 0
    lead_y = 0
    lead_x_change = 0
    lead_y_change = 0
    feed_x = random.randint(0, (display_width/block_size)-1)
    feed_x = feed_x*block_size
    feed_y = random.randint(0, (display_height/block_size)-1)
    feed_y = feed_y*block_size
    print(f"feed_x={feed_x} and feed_y={feed_y}")
    snakeList= []
    check =0
    store=0
    k=0
    mark = 0
    bonus= 0
    
    while not gameExit:
        while gameOver == True:
            
##            gameDisplay.fill(white)
##            message("Press A to -PLAY AGAIN- and X to -QUIT-",red)
            

            for event in pygame.event.get():
                
                f= pygame.mouse.get_pos()
                if  f[0]>=195 and f[0]<=300 and f[1]>=390 and f[1]<=409:
                    gameDisplay.blit(gameOverWindowenlarge,(0,0))
                elif f[0]>=463 and f[0]<=483 and f[1]>=14 and f[1]<=38:
                    gameDisplay.blit(cross,(0,0))
                else :
                    gameDisplay.blit(gameOverWindow,(0,0))
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if f[0]>=195 and f[0]<=300 and f[1]>=390 and f[1]<=409:
                        gameLoop()
                    if f[0]>=463 and f[0]<=483 and f[1]>=14 and f[1]<=38:
                        gameExit = True
                        gameOver = False
            message( f"Your Score = {bonus}", white, -240 , size = "small")
            pygame.display.update()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if temp == 276 or temp == 275:
                        continue
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    if temp == 276 or temp == 275:
                        continue
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    if temp == 273 or temp == 274:
                        continue
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    if temp == 273 or temp == 274:
                        continue
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
                elif event.key == pygame.K_SPACE:
                    pause()
                temp = event.key
            

        lead_x = lead_x + lead_x_change
        lead_y = lead_y + lead_y_change
       # print(f"lead_x={lead_x} and lead_y={lead_y}")
        if lead_x >= display_width or lead_x<0 or lead_y >= display_height or lead_y<0:
            gameOver = True
        if (lead_x == feed_x and lead_y ==feed_y)or mark>40:
            if mark<=40:
                snakeLength = snakeLength + 1
                mark=0
            k=0
            mark = 0
            while True:
                feed_x = random.randint(0, (display_width/block_size)-1)
                feed_x = feed_x*block_size
                feed_y = random.randint(0, (display_height/block_size)-1)
                feed_y = feed_y*block_size
                for x in snakeList:
                    if x[0]==feed_x and x[1]==feed_y:
                        k=1
                        break
                    else:
                        k=0
                print(f"true k={k}")
                if k==1:
                    continue
                else :
                    break
            
        k=0
        gameDisplay.blit(starBackground,(0,0))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del snakeList[0]
        if snakeLength>3:
            for x in snakeList[:-1]:
                if x == snakeHead:
                    gameOver= True
        check=check+1
        message("Score: ",white,y_displacement = -300 ,size = "large")
        if check<3:
            store=0
        else :
            store=1
        if check>6:
            check=0
        mark = mark+1
        snake(block_size,snakeList,snakeHead,direction,store)
        if store==0:
            gameDisplay.blit(fruitSmall,(feed_x,feed_y))
        else :
            gameDisplay.blit(fruitLarge,(feed_x,feed_y))
        clock.tick(FPS)
        bonus = str(snakeLength - 3)
        print(bonus)
        #message("PAUSED", red, -200,size = "medium")
        message( bonus, red, -200 , size = "small")
        pygame.display.update()
        
    pygame.quit()
    quit()
while True:   
    for event in pygame.event.get():
        z= pygame.mouse.get_pos()
##        gameDisplay.blit(gameOverWindow,(0,0))
        if z[0]>=170 and z[0]<=324 and z[1]>=212 and z[1]<=282:
            gameDisplay.blit(foregroundEnlarge,(0,0))
        else:
            gameDisplay.blit(foreground,(0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if z[0]>=170 and z[0]<=324 and z[1]>=212 and z[1]<=282:
                gameLoop()
        clock.tick(FPS)
        pygame.display.update()
