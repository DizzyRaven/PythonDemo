#Разделяем сущности на классы
class Things:
    pass
#==============================
#Потомки и предки
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    pass
class Mammals(Animals):
    pass
class Giraffes(Mammals):
    pass
#==============================
#Создаем объекты для классов
reginald = Giraffes()
#==============================
#Определение функций класса
#Вот обычная функция, не имеющая никакого отношения к классам:
"""def this_is_a_normal_function():
    print('Я обычная функция')"""
#А вот несколько функций, принадлежащих классу:
"""class ThisIsMySillyClass:
    def this_is_a_class_function():
        print('Я – функция класса')
    def this_is_also_a_class_function():
        print('Я тоже функция класса, понятно?')"""
#==============================
#Используем функции для задания характеристик класса
class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass
class Mammals(Animals):
    def feed_yound_with_milk(self):
        pass
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass
#==============================
#Зачем нужны классы и объекты?
class Animals(Animate):
    def breathe(self):
        print('Дышит')
    def move(self):
        print('Двигается')
    def eat_food(self):
        print('Ест')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('Кормит детенышей молоком')
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('Ест листья')
reginald = Giraffes()
#reginald.move()
#reginald.eat_leaves_from_trees()
harold = Giraffes()
#harold.move()
#==============================
#Объекты и классы в картинках
"""import turtle
avery = turtle.Pen()
kate = turtle.Pen()
avery.forward(50)
avery.right(90)
avery.forward(20)
kate.left(90)
kate.forward(100)
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)
kate.right(90)
kate.forward(80)
kate = turtle.Pen()
kate.right(90)
kate.forward(100)
kate.left(90)
kate.forward(30)"""
#==============================
#Другие полезные свойства объектов и классов
#Унаследованные функции
#==============================
#Функции, вызывающие другие функции
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print('Я нашел еду!')
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
"""reginald = Giraffes()
reginald.dance_a_jig()"""
#==============================
#Инициализация объектов
class Giraffes:
    def __init__(self, spots):
        self.giraffe_spots = spots
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)
#=====================================================================
