import random
from pynput.mouse import Controller
#from pynput.keyboard import Controller

def controlMouse():
    rand1 = random.randrange(0,1000)
    rand2 = random.randrange(0,1000)
    mouse = Controller()
    mouse.position = (rand1,rand2)
    #(left to right, top to bottom)
    #from top-left of the screen it is (0,0)

controlMouse()

#def controlKeyboard():
#    keyboard = Controller()
#    keyboard.type("Nigga bkl")

#controlKeyboard()