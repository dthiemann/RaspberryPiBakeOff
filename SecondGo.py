

import pygame, sys
from pygame.locals import *

import pygame

class Button():

    def __init__(self, width, height, x, y, color, text, textColor):
        self.width = width
        self.height = height
        self.xpos = x
        self.ypos = y
        # Make a new surface object for the text to live on
        surface = pygame.Surface((width,height))
        self.color = color
        # Load the font with the font size
        fonts = pygame.font.Font(None, 24)
        # Render the text
        displayText = fonts.render(text, 1, color)
        # Get the size of the rectangle the text is in
        textpos = displayText.get_rect()
        # Center the text within it's container
        textpos.centerx = surface.get_rect().centerx
        textpos.centery = surface.get_rect().centery
        # Blit it onto the surface object
        surface.blit(displayText,textpos)
        #Convert to improve render time
        surface.convert()
        self.surface = surface




pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((640,480))
questionFont = pygame.font.Font("freesansbold.ttf",32)
answerFont = pygame.font.Font("freesansbold.ttf",24)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,250,0))

buttonA = Button(150,150,300,300,(0,255,0),"Scoodly do bop", (0,0,0))
background.blit(buttonA.surface,(buttonA.xpos,buttonA.ypos))

screen.blit(background, (0,0))
pygame.display.flip()



ListOfQuestions = {'Question A: Yellow is what color?' : ["cheese", "blue","yellow","yesterday"]}

msgSurface = questionFont.render("Hello",True, (0,0,0))
answer11 = answerFont.render("Answer1", True, (0,0,0),(0,0,100))
screen.blit(msgSurface,(10,10))
screen.blit(answer11, (50,50))


x = ListOfQuestions.popitem()
while True:
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

# response = raw_input("If you want to proceed, enter 1 and hit enter")
# if response == "1":
#     continue

