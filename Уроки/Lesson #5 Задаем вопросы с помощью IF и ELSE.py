#Конструкция if
age = 27
if age > 20:
    print("Как то вы староваты!")
#=====================================================================
#Блок — это группа команд
#age = 25
#if age > 20:
#    print("Как-то вы староваты!")
#    print("Что вы здесь делаете?")
#    print("Почему не стрижете газон или не перекладываете бумажки?")
#== Равно
#!= Не равно
#> Больше
#< Меньше
#>= Больше или равно
#<= Меньше или равно
#age = 10
#if age > 10:
#    print("Вы слишком стары для моих шуток!")
#=====================================================================
#Конструкция if-then-else
#print("Хотите услышать грязную шутку?")
#age = 11
#if age == 12:
#    print("Свинья шлепнулась в грязь!")
#else:
#    print("Тсс! Это секрет.")
#=====================================================================
#Команды if и elif
#age = 11
#if age == 10:
#    print("Что выйдет, если клюква наденет штаны?")
#    print("Брюква!")
#elif age == 11:
#    print("Что сказала зеленая виноградина синей виноградине?")
#    print("Дыши! Дыши!")
#elif age == 12:
#    print("Что сказал 0 числу 8?")
#    print("Привет, ребята!")
#elif age == 13:
#    print("Что такое: на потолке сидит и хохочет?")
#    print("Муха-хохотуха!")
#else:
#    print("Что-что?")
#=====================================================================
#Объединение условий
#age = 12
#if age == 10 or age == 11 or age == 12 or age == 13:
#    print("13 + 49 + 84 + 155 + 97: что получится? Головная боль!")
#else:
#    print("Что-что?")
#==============================
#age = 13
#if age >= 10 and age <= 13:
#    print("13 + 49 + 84 + 155 + 97: что получится? Головная боль!")
#else:
#    print("Что-что?")
#=====================================================================
#Переменные без значения — None
#В языке Python пустое значение называется None,
#и оно говорит о том, что переменная ничего не содержит.
#myval = None
#print(myval)
#==============================
#myval = None
#if myval == None:
#    print("В переменной myval ничего нет")
#=====================================================================
#Разница между строками и числами
#age = "10"
#if age == 10:
#    print("Как лучше всего общаться с монстром?")
#    print("Издалека!")
#elif age == "10":
#    print("Строка!")
#==============================
#сделать из строки '10' число может функция int:
#age = "10"
#converted_age = int(age)
#==============================
# для преобразования числа в строку служит функция str:
#age = 10
#converted_age = str(age)
#==============================
#age = "10"
#converted_age = int(age)
#if converted_age == 10:
#    print("Как лучше всего общаться с монстром?")
#    print("Издалека!")
#==============================
#age = "10.5"
#converted_age = float(age)
#print(converted_age)
