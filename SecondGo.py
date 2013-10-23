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
        displayText = fonts.render(text, 1, textColor)
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
        surface.set_alpha(200)
        surface.convert()

        self.surface = surface

    #Provides a way to update the button
    def update(width,height,x,y,text,):
        self.width = width
        self.height = height
        self.xpos = x
        self.ypos = y
        self.color = color
        # Load the font with the font size
        fonts = pygame.font.Font(None, 24)
        # Render the text
        displayText = fonts.render(text, 1, self.textColor)
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
background.fill((0,179,219))

buttonA = Button(150,100,200,300,(1,1,1),"Scoodly do bop da diddly toodly tum ta scoot there young sir ta toodly", (255,255,255))
background.blit(buttonA.surface,(buttonA.xpos,buttonA.ypos))

screen.blit(background, (0,0))
pygame.display.flip()

#Dictionary of all my questions
LanguageArtsQuestions = {'Choose the sentence which uses correct grammar:' : ["Your funny, to!", "Its you’re birthday party!","It’s your turn.","It’s you’re job, too!", "The correct answer is: 'It's your turn.'", 'Well done!' ],
'Which words in the following sentence are not spelled correctly? “Bob and Sarah went too the park and played frisbey.”': ['and', 'frisbey', 'too', 'b and c', 'Sorry, the correct answer is frisbey and too (b and c)', 'Right!'], 'Which of the following words should be capitalized?': ['monday', 'spring', 'water', 'pencil', 'The answer is Monday,', 'Right!'], 'What punctuation mark comes at the end of a sentence to show excitement?': ['?', '!', '.', '&', 'This does: !', 'AWESOME!!!'], 'What is a conjunction?': ['A train station.', 'Two sentences connected to form one sentence.', 'A punctuation mark used to show excitement.', 'A really yummy kind of pizza', 'The answer is: two sentences connected to form one sentence.', 'Correct!'], 'What are some words used in a conjunction?': ['and', 'but', 'or', 'all of the above', 'And, but, and or are all words used in a conjunction.', 'Awesome!'], 'Which of the following words is a synonym for “big”?': ['gigantic', 'great', 'little', 'small', 'Gigantic is the correct answer, sorry.', 'Good job!'], 'What does the prefix anti- mean?': ['with', 'against', 'large', 'cold', 'Anti- means against, like antidote is a cure because it works against the illness!', 'Excellent!'], 'Which of the following is an example of an idiom?': ['It’s raining cats and dogs!', 'Have a holly jolly Christmas.', 'Keep an eye out for that one.', 'All of the above are examples of idioms.', 'An idiom is when you say something that is not meant to be taken literally, so all of the answers are correct, but D was the best answer.', 'Nice!'], 'Which of the following is an example of a possessive word': ["You're", "It's", "Their", "There", 'Sorry, your answer is incorrect. Their is an example of a possessive word.', 'NICE!']
}

ScienceQuestions = { 'What kind of rocks form inside of volcanoes?': ['metamorphic', 'sedimentary', 'igneous', 'daffodils', 'Igneous rocks form when lava cools downs.', 'Correct!'], 'What is the term given to baby frogs before they gain their legs?': ['Baby frogs', 'little green things', 'snakes', 'tadpoles', 'Aw man, the correct answer is tadpoles.', 'Neat-oh!'], 'What kind of rock forms after experiencing intense heat and pressure?': ['sedimentary', 'metamorphic', 'igneous', 'daffodils', 'Metamorphic is the correct answer', 'Nice one!'], 'What is the name of all the parts of our body that help digest food?': ['The digestion system', 'The heart', 'The feet', 'The skeleton', 'The digestion system is the name for all the parts of our body that work together to help digest food!', 'Nice one, smarty!'], 'Which of the following do plants use for food?': ['Hot dogs', 'Sunlight', 'Water', 'B & C', 'Plants use sunlight, water, and soil in order to get nutrients, and they convert sunshine into food through a process called photosynthesis', 'AWESOME!']

}

SocialStudiesQuestions = { 'What document did the colonies sign to get freedom from the British soldiers in the American revolution?' : ['A piece of notebook paper', 'The grand statement', 'The Declaration of Independence', 'The Bill of Rights', 'The Decleration of independence declared independence (freedom) from the King of England!',  'Good job!'], 'Who was the first president of the United States?': ['Abraham Lincoln', 'George Washington', 'Barak Obama', 'Ronald Reagan', 'Sorry, the correct answer is George Washington', 'Nice!'], 'On which continent is the United States of America located?': ['North America', 'South America', 'France', 'Africa', 'The correct answer is North America', 'Correct!'], 'Who is the current President of the United States?': ['Barak Obama', 'George Bush', 'Bill Clinton', 'Richard Nixon', 'Barak Obama was elected in 2008 and is now serving his second term as president.', 'Nice!'], 'What is the capital of the United States?': ['Nebraska', 'New York City', 'Chicago', 'Washington D.C.', 'Washington D.C. is the capitol of America, and it is where the presidents and their families reside', 'Well done!'], 'What is an example of a state in the midwest?': ['Virginia', 'California', 'New York', 'Iowa', 'The correct answer is Iowa!', 'Correct!'], 'What countries are right next to America?': ['Mexico and Canada', 'Egypt and Russia', 'Switzerland and China', 'Brazil and Australia', 'Mexico is on the southern border and Canada is on the northern border', 'Right!'], 'What is the capital of ILlinois?': ['Chicago', 'Bloomington', 'Texas', 'Springfield', 'The correct answer is Springfield', 'Correct!']
}

mathQuestions = { 'How many centimeters are in one meter?': ['10', '1', '100', '1000', 'The prefix cent- means 100, so there are 100 centimeters in a meter', 'Bingo!'], 'What is 4 squared?': ['16', '2', '1', '8', 'Taking the square of a number is the equivalent to multiplying the number by itself. 4squared = 4x4 = 16', 'Well done!'], 'Josie cuts 8 apples in half. She gives herself and each person in her class one half of an apple. Afterwards, she is left with one half an apple. How many people are in her classroom (including Josie)?': ['16', '8', '4', '15', 'Each apple gives you two halves, 8x2 - 16. If everyone eats one half and there is one half remaining, that means there are 15 people in the classroom.', 'Nice!'], 'Not counting thumbs, how many fingers and toes do 2 people normally have altogether?': ['18', '36', '2', '11', '8 fingers + 10 toes = 18. 18x2 = 36.', 'Correct-o!'], 'How many degrees are the angles in an equilateral (meaning all sides and angles are equal) triangle? Hint: a triangle has angles that must add up to 180 degrees.': ['90', '3', '60', '100', '180/3 = 60', 'You are right!'], 'Larry has a bag containing a red marble, a blue marble, and a pink marble. If he closes his eyes and picks out a marble randomly, what are the chances Larry will pick a red marble?' : ['1 in 3 chance', '1 in 1 chance', '3 in 3 chance', 'No chance', 'If there are 3 marbles and only 1 is red, that means Larry has a 1 in 3 chance!', 'Nice job!'], 'Solve: 6x5x2': ['30', '15', '60', '32', '6x5 = 30. 30x2 = 60. Better luck next time!', 'Neat!'], 'Put either "+", "x", "-", "÷" between 5, 10, 2, and 1 to try and get 51.': ['5x10÷2+1', '5÷10+2x1', '1+5+2+10', 'None of the above', '5x10÷2+1 = 51!', 'You rock!'], 'What is a prime number?': ['A really long number', 'A number only divisible by one and itself', 'The square root of 16', 'Zero', 'A number only divisible by one and itself', 'AWESOME!']
}

# msgSurface = questionFont.render("Hello",True, (0,0,0))
# answer11 = answerFont.render("Answer1", True, (0,0,0),(0,0,100))
# screen.blit(msgSurface,(10,10))
# screen.blit(answer11, (50,50))

GenerateQuestion = Button(150,40,400,1,(0,0,0),"Generate Question", (0,0,0))
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
    



