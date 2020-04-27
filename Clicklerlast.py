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
# while True:
#     clock.tick(10)# После 10 секунд должно идти выключение, но не происходит.
# pygame.quit()



def click_button():  # Функция для кнопки "клик"
    global clicks
    clicks += 1
    game.title("Количество кликов: {}".format(clicks))
    if clicks == 10:
        print(Back.RED + 'Открыто достижение: Начинающий кликермен!')
    if clicks == 50:
        print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
    if clicks == 15:
        level = 1
        print(Back.CYAN + 'Вы достигли', level ,'уровня!')
    if clicks == 100:
        print(Back.GREEN + "Открыто достижение: Первая соточка!")


def dclick_button():  # Функция для кнопки "двойной клик"
    global clicks
    clicks += 2
    game.title("Количество кликов: {}".format(clicks))
    if clicks == 10:
        print(Back.RED + 'Открыто достижение: Начинающий кликермен!')
    if clicks == 50:
        print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
    if clicks == 15:
        level = 1
        print(Back.CYAN + 'Вы достигли', level ,'уровня!')
    if clicks == 100:
        print(Back.GREEN + "Открыто достижение: Первая соточка!")


def levelM():
    global level
    global clicks
    if clicks == 15:
        level = 1
        print('Вы достигли', level, 'уровня!')


clicker = Tk()
game = Tk()






clicker.title("Кликер от IEM")
game.title("Количество кликов: 0")
clicker.geometry("1366x768")
game.geometry("315x0")

btn = Button(clicker, text="Клик", background="#444", foreground="#bbb",
             padx="20", pady="8", font="16", command=click_button)
btn.place(x='95', y='90')

btn2 = Button(clicker, text="Двойной клик", background="#222", foreground="#ccc",
              padx="20", pady="8", font="16", command=dclick_button)
btn2.place(x='50', y='150')
btn5 = Button(clicker, text="Старт", command=call_funcs, padx="20", pady="8", font="16")
btn5.place(x='50', y='250')



canvas =Canvas(clicker,width=960,height=768)
image=ImageTk.PhotoImage(Image.open('walk.jpg'))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
# btn = Button(clicker, text="Не нажимать!")
#btn.grid(column=0, row=3)

clicker.mainloop()
game.mainloop()
