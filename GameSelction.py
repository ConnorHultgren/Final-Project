import pygame
import time
import random
import Games.RPS
import Games.Pong
pygame.init()
pygame.font.init()

from pygame.locals import( #The inputs from the user
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_RETURN,
    K_UP,
    K_DOWN,
)

TitleFont = pygame.font.SysFont(pygame.font.get_default_font(), 60)

SubTitleFont = pygame.font.SysFont(pygame.font.get_default_font(), 40)

#Creates Window
WofW = 400
HofW = 400
window = pygame.display.set_mode([WofW,HofW]) #Window with 400x400 pixels

#Basic Menu
class Selection:

    def __init__(self):
        self.arrow_group = pygame.sprite.GroupSingle(Arrow()) #GroupSingle only allows for one sprite at a time 

    def draw(self, window): #Makes Things show up on window
        window.fill((0,0,0))

        #Title for Selection Menu
        text_surface = TitleFont.render("Choose a Game:", False, (255,255,255))
        window.blit(text_surface, (30,30))

        #First Game Option
        op1 = pygame.Surface((220,90))
        op1.fill((0,255,255))
        rect = op1.get_rect()

        window.blit(op1,((WofW-op1.get_width()-75)/2,(HofW-op1.get_height()-50)/2))

        text_surface = SubTitleFont.render("Pong", False, (0,0,0))
        window.blit(text_surface, (60,166))

        #Second Game Option
        op2 = pygame.Surface((220,90))
        op2.fill((0,255,255))
        rect = op2.get_rect()

        window.blit(op2,((WofW-op2.get_width()-75)/2,(HofW-op2.get_height()+200)/2))

        text_surface = SubTitleFont.render("Rock, Paper,", False, (0,0,0))
        window.blit(text_surface, (60,279))
        text_surface = SubTitleFont.render("Scissors!", False, (0,0,0))
        window.blit(text_surface, (60,306))

        self.arrow_group.draw(window) #Draws arrow once instead of once per frame
        pygame.display.flip()

#Player input
class Arrow(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Images/White_Arrow.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (330,168)

        
    def update(self, UpKey, DownKey):
        if UpKey:
            self.rect.center = (330,168)

        if DownKey:
            self.rect.center = (330,296)
  
running = True
Up = True
menu = Selection()
clock = pygame.time.Clock()  #Limit Frames



#Game Loop: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
while running == True:
    for event in pygame.event.get():
        if event.type == QUIT: #If quiting game, close window
            running = False
        if event.type == KEYDOWN: #If pressing escape, close window
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_DOWN:
                Up = False
            if event.key == K_UP:
                Up = True



            if event.key == K_RETURN and Up == True:
                Games.Pong.run_pong()
                print("Selected Pong")
            
            if event.key == K_RETURN and Up == False:
                Games.RPS.run_game()
                print("Seleted Rock-Paper-Scissors")


    UpKey = pygame.key.get_pressed()[K_UP]
    DownKey = pygame.key.get_pressed()[K_DOWN]

    menu.arrow_group.sprite.update(UpKey, DownKey)
    menu.draw(window)

    clock.tick(30)   #30 frames limit
