from tkinter import *
from tkinter import Tk, Button
from PIL import Image, ImageTk
import os
expression = "" 
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 
def ravno(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set("Ошибочка") 
        expression = "" 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
root = Tk()
equation = StringVar()
equation.set('Количество кликов: ')
expression_field = Entry(root, textvariable=equation) 
expression_field.grid(columnspan=4, ipadx=70) 
root.title("IEM Кликер")
root.geometry("320x300")
def create_window():
    window = Toplevel(root)
    image = ImageTk.PhotoImage(Image.open("C:/a/ZBWoVQuQytQ.jpg"))
    l = Label(window, image=image)
    l.image=image
    l.pack()
image = ImageTk.PhotoImage(Image.open("M:/Git/IEM2/homa.jpg"))
Button(root, image=image, command=create_window).grid(columnspan=1)
root.mainloop()