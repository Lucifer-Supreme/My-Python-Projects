#Running this program will result is deletion of all previous key strokes 
from pynput.keyboard import Listener

with open("log.txt",'w')as file:
    file.write("")
with open("log 2.txt",'w')as file:
    file.write("")