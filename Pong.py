import pygame
import random
import time
pygame.init()
pygame.font.init()

def run_pong():
    from pygame.locals import( #The inputs from the user
        QUIT,
        KEYDOWN,
        KEYUP,
        K_ESCAPE,
        K_DOWN,
        K_UP,
    )

    #TextSizes:
    TitleSize = pygame.font.SysFont(pygame.font.get_default_font(), 55)
    GameFont = pygame.font.SysFont(pygame.font.get_default_font(), 70)

    #Title
    Title = pygame.Surface((120,50))
    Title.fill((67,16,134))
    rect = Title.get_rect()

    WofW = 400
    HofW = 300
    window = pygame.display.set_mode([WofW,HofW]) #Window with 400x400 pixels

    #Paddle:
    paddle = pygame.Surface((7,45))
    paddle.fill((255,255,255))
    paddle_rect = paddle.get_rect()

    running = True
    clock = pygame.time.Clock()
    MoveU = None
    MoveD = None
    reset_delay = 0

    Ppos = HofW // 2 #Paddle will start in the middle, does not move on the x => only one coordinate
    Pspd = 5 #One number = speed of y

    Bpos = pygame.Rect(WofW // 2, HofW // 2, 10,10) #Ball starts in middle, Both x and y => needs both coordinates, rect for easy collision
    Bspd = [5,5] #Speed of x and speed of y

    #Game Loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    while running == True:
        for event in pygame.event.get():
            if event.type == QUIT: #If quiting game, close window
                running = False
            if event.type == KEYDOWN: #If pressing escape, close window
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_DOWN:
                    MoveD = True
                if event.key == K_UP:
                    MoveU = True
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    MoveD = False
                if event.key == K_UP:
                    MoveU = False

        if MoveU == True and Ppos >= 0:
            Ppos -= Pspd

        if MoveD == True and Ppos <= HofW - 45:
            Ppos += Pspd

        #Wall/Paddle Collision:
        Bpos.x += Bspd[0]
        Bpos.y += Bspd[1]

        if Bpos.bottom >= HofW: #Collision with bottom of rect instead of center
            Bspd[1] = - Bspd[1]

        if Bpos.top <= 0: #Collision with top ...
            Bspd[1] = - Bspd[1]

        if Bpos.left <= 0: #Collision with left side ...
            Bspd[0] = - Bspd[0]

        if Ppos <= Bpos[1] <= Ppos + 45 and Bpos[0] == 375:
            Bspd[0] = -Bspd[0]

        if Bpos.right >= WofW: #If hitting right wall, wait 90 frames (3s) then reset
            reset_delay += 1
            if reset_delay >= 90:
                Bpos.y = HofW // 2
                Bpos.x = WofW // 2
                reset_delay = 0

        window.fill((0,0,0)) #New Frame - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        #Loss:
        if reset_delay > 0:
            text_surface = GameFont.render("You Lose!", False, (255,0,0))
            window.blit(text_surface, (87,100))

        #Paddle:
        window.blit(paddle,(375,Ppos))

        #Show Title
        window.blit(Title,(7,7))
        text_surface = TitleSize.render("Pong", False, (0,0,0))
        window.blit(text_surface, (18,16))

        #Ball
        pygame.draw.circle(window,(255,255,255),Bpos.center, Bpos.width //2)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

