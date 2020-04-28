from tkinter import *
from colorama import init, Fore, Back
import pygame
import pyglet
from PIL import ImageTk, Image

init()

clicks = 0  # Переменная, в которой будут все клики
level = 0  # Уровень пользователя в игре

def clicked():
    btn5.configure(command=playsound())
    print(Back.YELLOW + "Открыто достижение: Вечеринка началась!")
    
def playsound() :
    pygame.init()
    song = pygame.mixer.music.load('hah.mp3')
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    
def call_funcs():
    playsound()
    global clicks
    if clicks % 2 ==0:
        clicked()

def click_button():  # Функция для кнопки "клик"
    global clicks
    clicks += 1
    clicker.title("Количество кликов: {}".format(clicks))
    if clicks == 10:
        print(Back.RED + 'Открыто достижение: Начинающий кликермен!')
    if clicks == 50:
        print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
    if clicks == 15:
        level = 1
        print(Back.CYAN + 'Вы достигли', level ,'уровня!')
    if clicks == 100:
        print(Back.GREEN + "Открыто достижение: Первая соточка!")
        print("Открыто достижение: Достижение не открыто, хватит кликать, спать иди!!!")

    def dclick_button():  # Функция для кнопки "двойной клик"
        global clicks
        clicks += 2
        clicker.title("Количество кликов: {}".format(clicks))
        if clicks == 15:
            level += 1
            print(Back.CYAN + 'Вы достигли', level ,'уровня!')
        if clicks == 10:
            print(Back.RED + 'Открыто достижение: Начинающий кликермен!')
        if clicks == 50:
            print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
        if clicks == 100:
            print(Back.GREEN + "Открыто достижение: Первая соточка!")
        if clicks == 10000:
            print("Открыто достижение: Достижение не открыто, хватит кликать, спать иди!!!")


def dclick_button():  # Функция для кнопки "двойной клик"
    global clicks
    clicks += 2
    clicker.title("Количество кликов: {}".format(clicks))
    if clicks == 10:
        print(Back.RED + 'Открыто достижение: Начинающий кликермен!')
    if clicks == 50:
        print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
    if clicks == 15:
        level = 1
        print(Back.CYAN + 'Вы достигли', level ,'уровня!')
    if clicks == 100:
        print(Back.GREEN + "Открыто достижение: Первая соточка!")
    if clicks == 10000:
        print("Открыто достижение: Достижение не открыто, хватит кликать, спать иди!!!")
    

def cheats():
    print("Введите чит-код:")
    cheat = input()
    if cheat == "da":
        print("Вам начислено 10000 кликов!")
        print(Back.RED + 'Открыто достижение: Начинающий кликермен!')
        print(Back.GREEN + "Открыто достижение: Первая соточка!")
        print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
        print(Back.MAGENTA + "Открыто достижение: Двести - всего-лишь цифра!")
        print(Fore.BLUE + Back.WHITE + "Открыто достижение: Достижение не открыто, хватит кликать, спать иди!!!")
    else:
        print("Неверный чит-код!")
clicker = Tk()
#game = Tk()

#clicker.title("Кликер от IEM")
clicker.title("Количество кликов: 0")
clicker.geometry("1366x768")
#game.geometry("315x0")

btn = Button(clicker, text="Клик", background="#444", foreground="#bbb",
             padx="20", pady="8", font="16", command=click_button)
btn.place(x='65', y='100')
#if level == 1:

 
btn5 = Button(clicker, text="Музон", command=call_funcs, padx="20", pady="8", font="16")#Музыка
btn5.place(x='55', y='200') 

#photo = PhotoImage("M:/Git/IEM2/cheats.png") 
#photoimage = photo.subsample(3, 3) 

btn6 = Button(clicker, text="Читы", command=cheats, highlightbackground='red', padx="20", pady="8", font="16")#Читы
btn6.place(x='55', y='250') 

btn2 = Button(clicker, text="Двойной клик", background="#222", foreground="#ccc", 
        padx="20", pady="8", font="16", command=dclick_button)            #Дабл клик
btn2.place(x='35', y='150')

canvas =Canvas(clicker,width=1000,height=768)#Изображение
image=ImageTk.PhotoImage(Image.open('walk.jpg'))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

clicker.mainloop()
#game.mainloop()
