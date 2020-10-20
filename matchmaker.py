import random
import time
from tkinter import Tk , Button , DISABLED

def show_symbol(x,y):
    # inorder to use variables which are also outside function its necessary to declare them as global inside functions
    global first
    global previousx , previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks() # Keeping you Tkinter display up to date while monitoring

    # now when a button is clicked previous x and y become the current one at first click
    if first:
        previousx = x
        previousy = y
        first = False    # to exit from here
    elif previousx != x or previousy != y:     # ie if the user doesnt click the same button ie he clicks some other button
        # we need to see if the text ie text of that symbol of the button user clicked first matches with the new button
        # that he just clicked
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            # as it didnt match so put it to sleep and empty the text so that nothing is visible
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            # what if the second click matches with the first one
            # you need to keep the button displaying
            # for that purpose disable the command to stuck them there at two certain positions ie first click n second click
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        # to execute the function the second time we again make the first True
        first = True

win = Tk() # started tkinter
win.title('Matchmaker')      # gave title
win.resizable(width=False , height=False)   # to fix the screen set the method parameters false
first = True   # an analogy that the button is clicked
# you play with previous x and y and the current x and y
previousx = 0
previousy = 0
# keeping buttons and symbols empty so that to add them later
buttons = { }
button_symbols = { }

# following are the emojis symbols , by typing which you will get certain emojis
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbols)     # shuffles the entities of lists randomly so that there may not be a fix pattern in the list


# x is the rows that are 6 and y is the column thats 4 now to plot them a matrix we will deploy a nested for loop
for x in range(6):
    for y in range(4):
        # now for every position of our matrix we need to create buttons
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 10, height = 8) # show_symbol funciton will be fired on clicking
        button.grid(column = x , row = y)  # will create a grid and position buttons according to x and y
        buttons[x,y] = button # redefining the buttons via its position
        button_symbols[x,y] = symbols.pop()

win.mainloop()
