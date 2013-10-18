import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((640,480))
questionFont = pygame.font.Font("freesansbold.ttf",32)
answerFont = pygame.font.Font("freesansbold.ttf",24)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,250,0))
screen.blit(background, (0,0))
pygame.display.flip()

ListOfQuestions = {'Question A: Yellow is what color?' : ["cheese", "blue","yellow","yesterday"]}

while ListOfQuestions:
    msgSurface = questionFont.render("Hello",True, (0,0,0))
    answer11 = answerFont.render("Answer1", True, (0,0,0),(0,0,100))
    screen.blit(msgSurface,(10,10))
    screen.blit(answer11, (50,50))


    x = ListOfQuestions.popitem()

    question1 = questionFont.render(x[0], True, (0,0,0))
    answer1 = answerFont.render(x[1][0],True, (0,0,0))
    answer2 = answerFont.render(x[1][1],True, (0,0,0))
    answer3 = answerFont.render(x[1][2],True, (0,0,0))
    answer4 = answerFont.render(x[1][3],True, (0,0,0))
    
    screen.blit(question1, (50,100))
    screen.blit(answer1, (50, 150))
    screen.blit(answer2, (50, 200))
    screen.blit(answer3, (300, 150))
    screen.blit(answer4, (300,200))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    response = raw_input("If you want to proceed, enter 1 and hit enter")
    if response == "1":
        continue
    
