#Создание копий с помощью модуля copy
"""class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
#harry = Animal('гиппогриф', 6, 'розовый')
import copy
#harriet = copy.copy(harry)
#print(harry.species)
#print(harriet.species)
harry = Animal('гиппогриф', 6, 'розовый')
carrie = Animal('химера', 4, 'в зеленый горошек')
billy = Animal('богл', 0, 'узорчатый')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
#print(more_animals[0].species)
#print(more_animals[1].species)
my_animals[0].species = 'вампир'
#print(my_animals[0].species)
#print(more_animals[0].species)
sally = Animal('сфинкс', 4, 'песочный')
my_animals.append(sally)
#print(len(my_animals))
#print(len(more_animals))
more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'дракон'
print(my_animals[0].species)
print(more_animals[0].species)"""
#=====================================================================
#Ключевые слова и модуль keyword
"""import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('ozwald'))
print(keyword.kwlist)"""
#=====================================================================
#Генерация случайных чисел с помощью модуля random
#Использование randint
"""import random
print(random.randint(1, 100))
print(random.randint(100, 1000))
print(random.randint(1000, 5000))"""
#==============================
"""import random
num = random.randint(1, 100)
while True:
    guess = input('Угадайте число от 1 до 100: ')
    i = int(guess)
    if int(i) == num:
        print('Правильно')
        break
    elif int(i) < num:
        print('Загаданное число больше')
    elif int(i) > num:
        print('Загаданное число меньше')"""
#=====================================================================
#import random
#desserts = ['Роллы', 'Бургеры', 'Гороховый Суп', 'Пицца', 'Баночка', 'Макарохи']
#print(random.choice(desserts))
#=====================================================================
#Перетасовка списка с помощью shuffle
"""import random
desserts = ['мороженое', 'блинчики', 'пирог', 'печенье', 'конфеты']
random.shuffle(desserts)
print(desserts)"""
#=====================================================================
#Выход из оболочки с помощью функции exit
#import sys
#sys.exit()
#=====================================================================
#Ввод данных и объект stdin
#import sys
#v = sys.stdin.readline()
#Тот, кто смеется последним, медленнее соображает
#print(v)
#==============================
#Одно из различий между input и readline состоит в том, что для
#readline можно задать ограничение количества символов. 
#v = sys.stdin.readline(13)
#Тот, кто смеется последним, медленнее соображает
#print(v)
#=====================================================================
#Вывод данных и объект stdout
#import sys
#sys.stdout.write("У какого слона нет хобота? У шахматного!")
#=====================================================================
#Какую версию Python я использую?
#import sys
#print(sys.version)
#=====================================================================
#Работа со временем и модуль time
"""import time
print(time.time())
def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print("Прошло %s секунд" % (t2 - t1))
lots_of_numbers(1000)"""
#=====================================================================
#Преобразование дат с помощью asctime
#import time
#print(time.asctime())
#==============================
"""import time
t = (2026, 6, 10, 12, 0, 0, 5, 0, 0)
print(time.asctime(t))"""
#=====================================================================
#Получаем дату и время с помощью localtime
"""import time
print(time.localtime())
t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)"""
#=====================================================================
#Делаем передышку с помощью sleep
"""import time
for x in range(1, 61):
    print(x)
    time.sleep(1)"""
#=====================================================================
#Модуль pickle и сохранение информации
#import pickle
"""game_data = {'позиция-игрока' : 'С23 В45',
             'карманы' : ['молоток', 'карманный нож', 'гладкий камень'],
             'рюкзак' : ['веревка', 'молоток', 'яблоко'],
             'деньги' : 158.50
             }
save_file = open('D:\\_MYDOC\\GitHub\\PythonDemo\\Test\\save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()"""
#==============================
""""load_file = open('D:\\_MYDOC\\GitHub\\PythonDemo\\Test\\save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()
print(loaded_game_data)"""
#=====================================================================
