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
import random
desserts = ['Роллы', 'Бургеры', 'Гороховый Суп', 'Пицца', 'Баночка', 'Макарохи']
print(random.choice(desserts))
















