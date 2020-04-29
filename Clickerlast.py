from tkinter import *
from colorama import init, Fore, Back
import pygame
import pyglet
from PIL import ImageTk, Image
import random

init()

clicks = 99  # Переменная, в которой будут все клики
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


def ruletka():
    global clicks
    if clicks >=170:
        clicks -= 60
        print('Вы открываете кейс! Он стоит 60 кликов!')
        prize = ['Чит-код', "50 кликов", "51 клик", "52 клика", "53 клика", "54 клика", "55 кликов", "56 кликов", "57 кликов", "58 кликов", "60 кликов", "61 клик", "62 клика", "63 клика", "64 клика", "65 кликов", "66 кликов", "67 кликов", "68 кликов", "69 кликов", "70 кликов",]
        win = random.choice(prize)
        print("Ваш приз - ", win)
        if win == 'Чит-код':
            print('Активация => Читы => В консоли написать BUTTON')
        elif win == '50 кликов':
            clicks += 50
        elif win == '51 клик':
            clicks += 51
        elif win == '52 клика':
            clicks += 52
        elif win == '53 клика':
            clicks += 53
        elif win == '54 клика':
            clicks += 54
        elif win == '55 кликов':
            clicks += 55
        elif win == '56 кликов':
            clicks += 56
        elif win == '57 кликов':
            clicks +=57
        elif win == '50 кликов':
            clicks += 57
        elif win == '58 кликов':
            clicks += 58
        elif win == '59 кликов':
            clicks += 59
        elif win == '60 кликов':
            clicks += 60
        elif win == '61 клик':
            clicks += 61
        elif win == '62 клика':
            clicks += 62
        elif win == '63 клика':
            clicks += 63
        elif win == '64 клика':
            clicks += 64
        elif win == '65 кликов':
            clicks += 65
        elif win == '66 кликов':
            clicks += 66
        elif win == '67 кликов':
            clicks += 67
        elif win == '68 кликов':
            clicks += 68           
        elif win == '69 кликов':
            clicks += 69
        elif win == '70 кликов':
            clicks += 70
    else:
        print(Back.RED + 'Недостаточно кликов!')
          
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
        b3 = Button(game1, text="Кейс", command=ruletka, bg='#aaa')
        b3.place(x='86',y='120', height=40, width=60)
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
l = Label(text='Всем привет!', bg='#aaa') 
l.place(x='0',y='0')
l1 = Label(text='Рекомендуем комбинировать', bg='#aaa')
l1.place(x='0', y='20')
l2 = Label(text='виды кликов(двойной и', bg='#aaa')
l2.place(x='0', y='40')
l3 = Label(text='обычный), дабы получить', bg='#aaa')
l3.place(x='0', y='60')
l4 = Label(text='все достижения', bg='#aaa')
l4.place(x='0', y='80')
#clicker.title("Кликер от IEM")
clicker.title("Количество кликов: 0")
clicker.geometry("1366x768")
#game.geometry("315x0")

btn = Button(clicker, text="Клик", background="#444", foreground="#bbb",
             padx="20", pady="8", font="16", command=click_button)
btn.place(x='45', y='110')

btn5 = Button(clicker, text="Музон", command=call_funcs, padx="20", pady="8", font="16")#Музыка
btn5.place(x='35', y='235') 

#photo = PhotoImage("M:/Git/IEM2/cheats.png") 
#photoimage = photo.subsample(3, 3) 

btn6 = Button(clicker, text="Читы", command=cheats, highlightbackground='red', padx="20", pady="8", font="16")#Читы
btn6.place(x='41', y='300') 

btn2 = Button(clicker, text="Двойной клик", background="#222", foreground="#ccc", state=DISABLED,
        padx="20", pady="8", font="16", command=dclick_button)            #Дабл клик
btn2.place(x='0', y='175')

btn2['state'] = 'disabled'

canvas =Canvas(clicker,width=1000,height=768)#Изображение
image=ImageTk.PhotoImage(Image.open('M:/Git/IEM2/walk.jpg'))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

clicker.mainloop()