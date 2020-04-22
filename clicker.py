from tkinter import *
from tkinter import Tk, Button
from PIL import Image, ImageTk
import os
import time


from tkinter import * 

clicks = 0 


def click_button(): 
    global clicks 
    clicks += 1 
    game.title("Количество кликов: {}".format(clicks)) 
    
clicker = Tk() 
game = Tk()

clicker.title("Кликер от IEM") 
game.title("Количество кликов: 0") 
clicker.geometry("300x250") 
game.geometry("315x0")


btn = Button(text="Click Me", background="#555", foreground="#ccc", 
padx="20", pady="8", font="16", command=click_button) 
btn.pack() 

clicker.mainloop()