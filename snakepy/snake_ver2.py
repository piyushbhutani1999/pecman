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
       #print(event)
       # this will provide all the events
        if event.type == pygame.QUIT:
           gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
                print(f"lead_x_change ={lead_x_change}")
                print(event.key)
        #moves only when key is long pressed
        #when we release the key after long pressing then event come:
        #KEYUP: K_left if we release left key
    lead_x = lead_x + lead_x_change 
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,[lead_x,300,10,10])
    clock.tick(30)
    pygame.display.update()
    #print(f"lead_x= {lead_x} and {event}")

pygame.quit()
quit()
