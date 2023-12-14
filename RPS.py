import pygame
import random
import time
pygame.init()
pygame.font.init()

def run_game():
    from pygame.locals import( #The inputs from the user
        QUIT,
        KEYDOWN,
        K_ESCAPE,
        K_r,
        K_p,
        K_s,
    )

    #TEXT SIZE
    SubTitleFont = pygame.font.SysFont(pygame.font.get_default_font(), 25)
    TitleFont = pygame.font.SysFont(pygame.font.get_default_font(), 36)
    GameFont = pygame.font.SysFont(pygame.font.get_default_font(), 70)
    RESULTFont = pygame.font.SysFont(pygame.font.get_default_font(), 50)
    ComFont = pygame.font.SysFont(pygame.font.get_default_font(), 32)

    WofW = 400
    HofW = 400
    window = pygame.display.set_mode([WofW,HofW]) #Window with 400x400 pixels

    #RECT for Winner Display:
    Win = pygame.Surface((370,70))
    Win.fill((220,247,82))
    rect = Win.get_rect()

    #Images/Surfaces:
    rock = pygame.image.load("Images/Rock.png")
    rock = pygame.transform.scale(rock, (50,50))
    rock_rect = rock.get_rect(center=(83,300))

    #For ComChoice
    rock2 = pygame.transform.scale(rock, (50,50))
    rock2_rect = rock.get_rect(center=(300,130))

    #Display
    paper = pygame.image.load("Images/Paper.png")
    paper = pygame.transform.scale(paper, (50,50))
    paper_rect = paper.get_rect(center=(183,300))

    #For ComChoice
    paper2 = pygame.transform.scale(paper, (50,50))
    paper2_rect = paper.get_rect(center=(300,130))

    #DIsplay
    scissors = pygame.image.load("Images/Scissors.png")
    scissors = pygame.transform.scale(scissors, (50,50))
    scissors_rect = scissors.get_rect(center=(292,300))

    #For ComChoice
    scissors2 = pygame.transform.scale(scissors, (50,50))
    scissors2_rect = scissors.get_rect(center=(300,130))

    running = True
    clock = pygame.time.Clock()
    Winner = None
    Choice = None
    ComChoice = None
    Score = 0

    #Game Loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    while running == True:
        for event in pygame.event.get():
            if event.type == QUIT: #If quiting game, close window
                running = False
            if event.type == KEYDOWN: #If pressing escape, close window
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_r:
                    Choice = "Rock"
                elif event.key == K_p:
                    Choice = "Paper"
                elif event.key == K_s:
                    Choice = "Scissors"

                ComChoice = random.choice(["Rock", "Paper", "Scissors"])

                #W/L Scenarios:
                if Choice == "Rock" and ComChoice == "Scissors":
                    Winner = "YOU"
            
                if Choice == "Rock" and ComChoice == "Rock":
                    Winner = "TIE!"
            
                if Choice == "Rock" and ComChoice == "Paper":
                    Winner = "Computer"
            
                if Choice == "Paper" and ComChoice == "Scissors":
                    Winner = "Computer"
            
                if Choice == "Paper" and ComChoice == "Rock":
                    Winner = "YOU"
            
                if Choice == "Paper" and ComChoice == "Paper":
                    Winner = "TIE!"
            
                if Choice == "Scissors" and ComChoice == "Scissors":
                    Winner = "TIE!"
            
                if Choice == "Scissors" and ComChoice == "Rock":
                    Winner = "Computer"
            
                if Choice == "Scissors" and ComChoice == "Paper":
                    Winner = "YOU"
            
        window.fill((0,0,0)) #No images from past frames leftover

        #Score in Upper Lefthand
        text_surface = SubTitleFont.render(str(Score), False, (255,255,255))
        window.blit(text_surface, (377,13))

        #The Result
        window.blit(Win, (15,180))
        text_surface = RESULTFont.render("The Result:", False, (0,0,0))
        window.blit(text_surface, (20,200))

        if Winner == "YOU":
            text_surface = TitleFont.render("You Win!", False, (0,0,0))
            window.blit(text_surface, (227,206))
            Score += 1

        if Winner == "TIE!":
            text_surface = TitleFont.render("A Tie!", False, (0,0,0))
            window.blit(text_surface, (240,206))

        if Winner == "Computer":
            text_surface = ComFont.render("Computer Wins", False, (0,0,0))
            window.blit(text_surface, (216,208))

        #Directions
        text_surface = SubTitleFont.render("Rock (r)", False, (255,255,255))
        window.blit(text_surface, (50,350))

        text_surface = SubTitleFont.render("Paper (p)", False, (255,255,255))
        window.blit(text_surface, (150,350))

        text_surface = SubTitleFont.render("Scissors (s)", False, (255,255,255))
        window.blit(text_surface, (250,350))

        #UI
        text_surface = TitleFont.render("Computer's Choice:", False, (255,255,255))
        window.blit(text_surface, (20,120))
    
        #TITLE:
        text_surface = GameFont.render("ROCK,", False, (255,0,0))
        window.blit(text_surface, (6,4))

        text_surface = GameFont.render("PAPER,", False, (0,255,0))
        window.blit(text_surface, (166,4))

        text_surface = GameFont.render("SCISSORS!", False, (0,0,255))
        window.blit(text_surface, (6,49))

        #Show what Computer Chose
        if ComChoice == "Rock":
            window.blit(rock2, rock2_rect)

        if ComChoice == "Paper":
            window.blit(paper2, paper2_rect)

        if ComChoice == "Scissors":
            window.blit(scissors2, scissors2_rect)
        
        window.blit(rock, rock_rect)
        window.blit(paper, paper_rect)
        window.blit(scissors, scissors_rect)

        pygame.display.flip()
        clock.tick(30)   #30 frames /s

        #Reset after a time
        time.sleep(3)

        Winner = None
        Choice = None
        ComChoice = None

    pygame.quit()
