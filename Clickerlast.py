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
        print(Back.RED + 'Открыто достижение: Тише едешь - дальше будешь!')
    if clicks == 50:
        print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
    if clicks == 100:
        level = 1
        print(Back.CYAN + 'Вы достигли', level ,'уровня!')
        game1 = Tk()
        def switch():
            if btn2["state"] == "disabled":
                btn2["state"] = "active"
                b2["text"] = "Куплено!"
            else:
                b2["text"] = "Куплено!"
        game1.title('Магазин')
        game1.geometry("217x230")
        #--Buttons
        #b1 = Button(game1, text="Button", height=5, width=7)
        #b1.place(x='20', y='0')    
        b2 = Button(game1, text="Купить x2 клик", command=switch, background='#111', foreground='#bbb')
        b2.place(x='70', y='90')
        game1.mainloop()
    if clicks == 100:
        print(Back.GREEN + "Открыто достижение: Первая соточка!")
    if clicks == 200:   
        print(Back.MAGENTA + "Открыто достижение: Двести - всего-лишь цифра!")
    if clicks == 500:
            print(Back.YELLOW + 'Открыто достижение: 5 раз по 100!' )
    if clicks == 10000:
        print("Открыто достижение: Достижение не открыто, хватит кликать, спать иди!!!")
        
def dclick_button():  # Функция для кнопки "двойной клик"
        global clicks
        clicks += 2
        clicker.title("Количество кликов: {}".format(clicks))
        if clicks == 100:
            level = 1
            print(Back.CYAN + 'Вы достигли', level ,'уровня!')
        if clicks == 10:
            print(Back.RED + 'Открыто достижение: Тише едешь - дальше будешь!')
        if clicks == 50:
            print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
        if clicks == 100:
            print(Back.GREEN + "Открыто достижение: Первая соточка!")
        if clicks == 200:   
            print(Back.MAGENTA + "Открыто достижение: Двести - всего-лишь цифра!")
        if clicks == 500:
            print(Back.YELLOW + 'Открыто достижение: 5 раз по 100!' )
        if clicks == 10000:
            print("Открыто достижение: Достижение не открыто, хватит кликать, спать иди!!!")

def cheats():
    print("Введите чит-код:")
    cheat = input()
    if cheat == "da":
        print("Вы открыли все достижения!")
        print(Back.RED + 'Открыто достижение: Начинающий кликермен!')
        print(Back.GREEN + "Открыто достижение: Первая соточка!")
        print(Back.YELLOW + "Открыто достижение: На пути к чему-то большему!")
        print(Back.MAGENTA + "Открыто достижение: Двести - всего-лишь цифра!")
        print(Back.YELLOW + 'Открыто достижение: 5 раз по 100!' )
        print(Fore.BLUE + Back.WHITE + "Открыто достижение: Достижение не открыто, хватит кликать, спать иди!!!")
    else:
        print("Неверный чит-код!")
clicker = Tk()
#game = Tk()
l = Label(text='Всем привет!') #\n Рекомендуем комбинировать виды кликов(двойной и простой), \n дабы получить все достижения!')
l.place(x='0',y='0')
l1 = Label(text='Рекомендуем комбинировать')
l1.place(x='0', y='20')
l2 = Label(text='виды кликов(двойной и')
l2.place(x='0', y='40')
l3 = Label(text='обычный), дабы получить')
l3.place(x='0', y='60')
l4 = Label(text='все достижения')
l4.place(x='0', y='80')
#clicker.title("Кликер от IEM")
clicker.title("Количество кликов: 0")
clicker.geometry("1366x768")
#game.geometry("315x0")

btn = Button(clicker, text="Клик", background="#444", foreground="#bbb",
             padx="20", pady="8", font="16", command=click_button)
btn.place(x='65', y='100')

btn5 = Button(clicker, text="Музон", command=call_funcs, padx="20", pady="8", font="16")#Музыка
btn5.place(x='55', y='200') 

#photo = PhotoImage("M:/Git/IEM2/cheats.png") 
#photoimage = photo.subsample(3, 3) 

btn6 = Button(clicker, text="Читы", command=cheats, highlightbackground='red', padx="20", pady="8", font="16")#Читы
btn6.place(x='55', y='250') 

btn2 = Button(clicker, text="Двойной клик", background="#222", foreground="#ccc", state=DISABLED,
        padx="20", pady="8", font="16", command=dclick_button)            #Дабл клик
btn2.place(x='35', y='150')

btn2['state'] = 'disabled'

canvas =Canvas(clicker,width=1000,height=768)#Изображение
image=ImageTk.PhotoImage(Image.open('M:/Git/IEM2/walk.jpg'))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

clicker.mainloop()