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

#Dictionary of all my questions
ListOfQuestions = {'Question A: Yellow is what color?' : ["cheese", "blue","yellow","yesterday"]
                   }

msgSurface = questionFont.render("Hello",True, (0,0,0))
answer11 = answerFont.render("Answer1", True, (0,0,0),(0,0,100))
screen.blit(msgSurface,(10,10))
screen.blit(answer11, (50,50))

GenerateQuestion = Button(150,30,400,1,(0,255,0),"Generate Question", (255,255,255))
screen.blit(GenerateQuestion.surface,(GenerateQuestion.xpos,GenerateQuestion.ypos))


while True:

    buttonXwin = [x for x in range(400,551)]
    buttonYwin = [y for y in range(1,31)]

    answer = "A"
    userAnswer = ""

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == MOUSEBUTTONDOWN):
            print "Mouse clicked!"
            if (pygame.mouse.get_pos()[0] in buttonXwin) and (pygame.mouse.get_pos()[1] in buttonYwin):
                if (not ListOfQuestions):
                    print "The dictionary is empty"
                else: 
                    x = ListOfQuestions.popitem()

                    #Question and answer statements
                    question1 = questionFont.render(x[0], True, (0,0,0))
                    answer1 = answerFont.render("A: " + x[1][0], True, (0,0,0))
                    answer2 = answerFont.render("B: " + x[1][1], True, (0,0,0))
                    answer3 = answerFont.render("C: " + x[1][2], True, (0,0,0))
                    answer4 = answerFont.render("D: " + x[1][3], True, (0,0,0))

                    #Options Buttons
                    Abutton = Button(30,30,50,300, (255,255,255),"A",(0,255,0))
                    Axwin = [x for x in range(50,81)]
                    Aywin = [y for y in range(300,331)]
                    Bbutton = Button(30,30,50,350, (255,255,255),"B",(0,255,0))
                    Bxwin = [x for x in range(50,81)]
                    Bywin = [y for y in range(350,381)]
                    Cbutton = Button(30,30,100,300, (255,255,255), "C", (0,255,0))
                    Cxwin = [x for x in range(100,131)]
                    Cywin = [y for y in range(300,331)]
                    Dbutton = Button(30,30,100, 350, (255,255,255), "D", (0,255,0))
                    Dxwin = [x for x in range(100,131)]
                    Dywin = [y for y in range(350,381)]

                    screen.blit(question1, (50,100))
                    screen.blit(answer1, (50,150))
                    screen.blit(answer2, (50,200))
                    screen.blit(answer3, (300,150))
                    screen.blit(answer4, (300,200))
                    screen.blit(Abutton.surface,(Abutton.xpos,Abutton.ypos))
                    screen.blit(Bbutton.surface,(Bbutton.xpos,Bbutton.ypos))
                    screen.blit(Cbutton.surface,(Cbutton.xpos,Cbutton.ypos))
                    screen.blit(Dbutton.surface,(Dbutton.xpos,Dbutton.ypos))
            if (pygame.mouse.get_pos()[0] in Axwin) and (pygame.mouse.get_pos()[1] in Aywin):
                userAnswer = "A"
                print "You picked A"
            if (pygame.mouse.get_pos()[0] in Bxwin) and (pygame.mouse.get_pos()[1] in Bywin):
                userAnswer = "B"
                print "You picked B"
            if (pygame.mouse.get_pos()[0] in Cxwin) and (pygame.mouse.get_pos()[1] in Cywin):
                userAnswer = "C"
                print "You picked C"
            if (pygame.mouse.get_pos()[0] in Dxwin) and (pygame.mouse.get_pos()[1] in Dywin):
                userAnswer = "D"
                print "You picked D"
            
    pygame.display.update()



