#Speed Kombat.py
#This is a game
#Author: EricMGS
#Date: april 2018

#Imports
from tkinter import *
from tkinter import messagebox
import time
import sys
from random import *

#Variables
p1_x = 683
p1_y = 384
p1_function = 0
speed = 1
square_x = 0
square_y = 0
q_times = 20

#Functions

def square_rnd ():
    global square_x
    global square_y
    square_x = randrange (10, 1356)
    square_y = randrange (10, 635)
    square.place (x = square_x, y = square_y, anchor = CENTER)

def verify():
    global speed
    global square_x
    global square_y
    global p1_x
    global p1_y
    global q_times
    if p1_x > (square_x - 10) and p1_x < (square_x + 10) and p1_y > (square_y - 10) and p1_y < (square_y + 10):
        square_rnd()
        speed += 1.5
        q_times -= 1
        times.configure(text = (q_times, 'restantes'))
        if q_times == 0:
            messagebox.showinfo ('Fim', 'Você ganhou')
            sys.exit ()

def p1_right (event):
    global p1_x
    global p1_function
    global speed
    p1_function = 1
    while p1_x < 1361:
        if p1_function == 1:
            verify()
            if p1_x + speed < 1361:
                p1_x += speed
                player1.place (x = p1_x, anchor = CENTER)
                window.update ()
                time.sleep (0.01)
            else:
                player1.place (x = 1361, anchor = CENTER)
                return
        else:
            return
    return

def p1_left (event):
    global p1_x
    global p1_function
    global speed
    p1_function = 2
    while p1_x > 5:
        if p1_function == 2:
            verify()
            if p1_x - speed > 5:
                p1_x -= speed
                player1.place (x = p1_x, anchor = CENTER)
                window.update()
                time.sleep (0.01)
            else:
                player1.place (x = 5, anchor = CENTER)
                return
        else:
            return
    return

def p1_up (event):
    global p1_y
    global p1_function
    global speed
    p1_function = 3
    while p1_y > 5:
        if p1_function == 3:
            verify()
            if p1_y - speed > 5:
                p1_y -= speed
                player1.place (y = p1_y, anchor = CENTER)
                window.update ()
                time.sleep (0.01)
            else:
                player1.place (y = 5, anchor = CENTER)
                return
        else:
            return
    return

def p1_down (event):
    global p1_y
    global p1_function
    global speed
    p1_function = 4
    while p1_y < 663:
        if p1_function == 4:
            verify()
            if p1_y + speed < 663:
                p1_y += speed
                player1.place (y = p1_y, anchor = CENTER)
                window.update ()
                time.sleep (0.01)
            else:
                player1.place (y = 663, anchor = CENTER)
                return
        else:
            return
    return

#Window Configurations
window = Tk ()
window.attributes ('-fullscreen', True)
window.title ('Speed Kombat')
window.configure (bg = 'Gray70')

#Frames
player1 = Frame(width = 10, height = 10, bg = 'Blue')
player1.place (x = p1_x, y = p1_y, anchor = CENTER)

square = Frame (width = 10, height = 10, bg = 'Black')

division = Frame (width = 1366, height = 100, bg = 'White')
division.place (relx = 0.5, rely = 1, anchor = S)

#Labels
instruction = Label (text = 'Você é o quadrado azul\nVocê deve pegar o quadrado preto 20 vezes\nUse as setas direcionais', bg = 'white', font = ('arial bold', 15))
instruction.place (relx = 0.3, rely = 0.93, anchor = CENTER)

times = Label (text = (q_times, 'restantes'), font = ('impact', 20), bg = 'white')
times.place (relx = 0.8, rely = 0.93, anchor = CENTER)

#Binds
window.bind ('<Right>', p1_right)
window.bind ('<Left>', p1_left)
window.bind ('<Up>', p1_up)
window.bind ('<Down>', p1_down)


square_rnd ()

window.mainloop ()
