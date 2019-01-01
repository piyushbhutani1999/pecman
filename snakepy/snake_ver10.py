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
##  gives message to screen
font = pygame.font.SysFont(None, 25)
## SysFont is a font type and 25 is the sixe of the font
def message(msg,color):
    screen_text = font.render(msg , True , color)
    gameDisplay.blit(screen_text, [(display_width/3)-80 , display_height/2])
    #blit function help in showing the text to screen [x and y cordinate of showing]

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
    perx =  feed_x
    pery = feed_y
    snakeList= []
    check =0
    store=0
    k=0
    move =1
    moveList = [20]
    moveList2 = [0]
    new_feed_x=0
    new_feed_y=0
    
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
                elif event.key == pygame.K_p:
                    yo = True
                    while(yo):
                        if event.key == pygame.K_p:
                            yo = False
                temp = event.key
            

        lead_x = lead_x + lead_x_change
        lead_y = lead_y + lead_y_change
       # print(f"lead_x={lead_x} and lead_y={lead_y}")
        if lead_x >= display_width or lead_x<0 or lead_y >= display_height or lead_y<0:
            gameOver = True
            
        if lead_x == perx and lead_y ==pery:
            snakeLength = snakeLength + 1
            k=0
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
        if move ==1:
            new_feed_x =feed_x +  20
            new_feed_y =feed_y +  0
            move =0
        if check<=3:
            store=0
        else :
            store=1
        if check>6:
            check=0
            move =1
        snake(block_size,snakeList,snakeHead,direction,store)
        if store==0:
            gameDisplay.blit(fruitLarge,(feed_x,feed_y))
            perx = feed_x
            pery = feed_y
            print(f"yes {feed_x} and {feed_y}")
        else :
            gameDisplay.blit(fruitLarge,(new_feed_x,new_feed_y))
            perx = new_feed_x
            pery =  new_feed_y
            print(f"no {feed_x} and {feed_y}")
        print(f"check= {check} move = {move} feed x y ={feed_x} {feed_y} new feed {new_feed_x} {new_feed_y}")
        if check == 6:
            feed_x = new_feed_x
            feed_y = new_feed_y
        clock.tick(FPS)
        pygame.display.update()
        
    pygame.quit()
    quit()
gameLoop()
