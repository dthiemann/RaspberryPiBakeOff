import pygame, sys, textwrap
from pygame.locals import *
import pygame

# class TextRectException:
#     def __init__(self, message = None):
#         self.message = message
#     def __str__(self):
#         return self.message

# Creates a Surface object which contains word
def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """

    
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 10
    for line in final_lines:
        # if accumulated_height + font.size(line)[1] >= rect.height:
        #     raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException, "Invalid justification argument: " + str(justification)
        accumulated_height += font.size(line)[1]

    return surface



class QuestionPane():

    def __init__(self, width, height, x, y, color, text, textColor):
        self.width = width
        self.height = height
        self.xpos = x
        self.ypos = y
        self.color = color
        # Load the font with the font size
        fonts = pygame.font.Font(None, 24)
        #makes a rectangle slightly larger than the declared width. I've
        #found this makes it look more centered
        rectangle = pygame.Rect((0,0), (width + 30,height))
        #Createds a Surface object that contains the text with line breaks
        text = render_textrect(text,fonts, rectangle,textColor,color, 1)
        self.surface = text

class Button():

    def __init__(self, width, height, x, y, color, text, textColor):
        self.width = width
        self.height = height
        self.xpos = x
        self.ypos = y
        self.color = color
        # Load the font with the font size
        fonts = pygame.font.Font(None, 24)
        # Render the text
        displayText = fonts.render(text, 1, color)
        # Get the size of the rectangle the text is in
        textpos = displayText.get_rect()
        # Make a new surface object for the text to live on
        surface = pygame.Surface((textpos.width+30,textpos.height + 30))
        # Center the text within it's container
        textpos.centerx = surface.get_rect().centerx
        textpos.centery = surface.get_rect().centery
        # Blit it onto the surface object
        surface.blit(displayText,textpos)
        #Convert to improve render time
        surface.convert()
        self.surface = surface

    #Provides a way to update the button
    def update(width,height,x,y,text):
        self.width = width
        self.height = height
        self.xpos = x
        self.ypos = y
        self.color = color
        # Load the font with the font size
        fonts = pygame.font.Font(None, 24)
        # Render the text
        displayText = fonts.render(text, 1, color)
        # Get the size of the rectangle the text is in
        textpos = displayText.get_rect()
        # Make a new surface object for the text to live on
        surface = pygame.Surface((textpos.width+30,textpos.height + 30))
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

buttonA = Button(150,100,200,300,(0,255,0),"Scoodly do bop da diddly toodly tum ta scoot there young sir ta toodly", (255,0,0))
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

GenerateQuestion = Button(150,40,400,1,(0,255,0),"Generate Question", (255,0,225))
screen.blit(GenerateQuestion.surface,(GenerateQuestion.xpos,GenerateQuestion.ypos))


while True:

    Xwin = [x for x in range(400,551)]
    Ywin = [y for y in range(1,31)]

    answer = "A"
    userAnswer = ""

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == MOUSEBUTTONDOWN):
            print "Mouse clicked!"
            if (pygame.mouse.get_pos()[0] in Xwin) and (pygame.mouse.get_pos()[1] in Ywin):
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



