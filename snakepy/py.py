import pygame
import time
import random
#font = pygame.font.SysFont(None,25)
#def message_to_screen(msg,color):
 #   screen_text = font.render(msg,True,color)
  #  game.Display.blit(screen_text,[490/2,490/2])
black=(0,0,0)
red=(255,0,0)
width = 490
height = 490
lead_x=0
lead_y=0
x=280
y=280
width_snake = 7
no_of_feed=1
height_snake = 7
feed_x = random.randint(0,71)
feed_x=feed_x*7
feed_y = random.randint(0,71)
feed_y = feed_y*7
clock = pygame.time.Clock()
print("feed")
print(feed_x)
print(feed_y)
def snake(snakelist):
    for XNY in snakelist:
        pygame.draw.rect(gameDisplay,black,[XNY[0],XNY[1],width_snake,height_snake])
        pygame.display.update()
        

gameDisplay = pygame.display.set_mode((width,height))
#sets our screen siur screen size
pygame.display.set_caption("Feed The Snake")
#sets screen caption on top


run = True
while run:
    gameDisplay.fill((255,255,255))
    for event in pygame.event.get():
    #it gives information about each and every event either the mouse move or key click
    #you can check this by print (event)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                lead_x = -width_snake
                lead_y = 0
            if event.key==pygame.K_RIGHT:
                lead_x = width_snake
                lead_y=0
            if event.key==pygame.K_UP:
                lead_y = -width_snake
                lead_x = 0
            if event.key==pygame.K_DOWN:
                lead_y = width_snake
                lead_x = 0
        if event.type==pygame.QUIT:
            #pygame.Quit is the cross ton the top right which quits the game
            run=False
            break
    x = x + lead_x
    y = y + lead_y
    snakeHead = [] 
    snakeList = []
    snakeHead.append(x)
    snakeHead.append(y)
    snakeList.append(snakeHead)
    snake(snakeList)
    if x==feed_x and y==feed_y:
        feed_x = random.randint(0,71)
        feed_x=feed_x*7
        feed_y = random.randint(0,71)
        feed_y = feed_y*7
        no_of_feed=no_of_feed + 1
        
    print(x),print (y),print(feed_x),print(feed_y)
    pygame.draw.rect(gameDisplay,red,[feed_x,feed_y,7,7])
    # also we can use gameDisplay.fill(black,rect=[x,y,width,height])
    #help in drawing the rect. [x,y,width,height]
    pygame.display.update()
    clock.tick(21)
pygame.quit()
quit()
