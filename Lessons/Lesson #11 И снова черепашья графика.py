#Начнем с обычного квадрата
#import turtle
#t = turtle.Pen()
"""t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.reset()"""
#==============================
"""for x in range(0, 4):
    t.forward(50)
    t.left(90)"""
#=====================================================================
#Рисуем звезды
""""for x in range(1, 9):
    t.forward(100)
    t.left(225)"""
#==============================
"""for x in range(1, 38):
    t.forward(100)
    t.left(175)"""
#==============================
"""for x in range(0, 190):
    t.forward(100)
    t.left(95)"""
#==============================
"""for i in range(0, 25):
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(110)
    t.forward(40)"""
#==============================
"""for x in range(0, 18):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)"""
#==============================
import turtle
t = turtle.Pen()
"""t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()

t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()"""
#==============================
#Возьмемся за краски
"""t.color(0, 1, 1)
t.begin_fill()
t.circle(50)
t.end_fill()"""
#=====================================================================
#Функция для рисования заполненной окружности
""""def mycircle(red, green, blue, size):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
mycircle(0, 1, 0.5, 40)"""
#mycircle(0.9, 0.75, 0, 50)
#mycircle(1, 0.7, 0.75, 50)
#=====================================================================
#Получение черного и белого цвета
#mycircle(0, 0, 0, 50)#Black
#mycircle(1, 1, 1, 50)#White
#=====================================================================
#Функция рисования квадрата
def mysquare(size):
    for x in range(0, 4):
        t.forward(size)
        t.left(90)
"""
mysquare(50)
t.reset()
mysquare(25)
mysquare(50)
mysquare(75)
mysquare(100)
mysquare(125)"""

#==============================
"""def my_blacksquare(red, green, blue, size):
    t.color(red, green, blue)
    t.begin_fill()
    for x in range(0, 4):
        t.forward(size)
        t.left(90)
    t.end_fill()

my_blacksquare(0, 0, 0, 175)
my_blacksquare(1, 1, 1, 150)
my_blacksquare(1, 0, 1, 150)
my_blacksquare(0, 0, 1, 125)
my_blacksquare(0, 1, 0, 100)
my_blacksquare(1, 0, 0, 75)
my_blacksquare(0, 1, 1, 50)
my_blacksquare(1, 1, 0, 25)"""
#=====================================================================
#Рисуем заполненные квадраты
"""t.begin_fill()
mysquare(50)
t.end_fill()"""
#==============================
""""def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()

mysquare(50, True)
mysquare(150, False)"""
#=====================================================================
"""def mystar(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()
        
t.color(0.9, 0.75, 0)
mystar(120, True)
t.color(0, 0, 0)
mystar(120, False)
"""
