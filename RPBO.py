import pygame
from Tkinter import *

'''
class MainApp():

    width, height = 640, 480
    screen = pygame.display.set_mode((width,height))

MainApp()


class MainApp():
    app = Tk()
    app.title("Raspberry Pi Bake-Off")
    app.geometry('640x480')

    app.mainloop()

    def quitApp():
        app.destroy()

    quitButton = Button(app,text = "quit", width = 10, commmand = quitApp)
    quitButton.pack(size = 'left')
'''

app = Tk()
app.title("Raspberry Pi Bake-Off")
app.geometry('640x480')

def quitApp():
    app.destroy()

quitButton = Button(app, text = 'quit', width = 10, command = quitApp)
quitButton.pack()

questionFrame = Canvas(app,width=640,height = 300, background = 'blue')
questionFrame.pack(side = 'bottom')

Label(questionFrame,text =" Questions?", font  = ("Times",32)).pack(side = 'top')
Label(questionFrame,text = "Baloons", font = ("Times",16)).pack(side = 'bottom')
#Label(questionFrame).grid(sticky = W)


app.mainloop()
