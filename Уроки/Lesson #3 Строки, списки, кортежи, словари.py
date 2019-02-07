#Строки
#fred = "Почему у горилл большие ноздри? Потому что у них толстые пальцы!"
#print(fred)
#fred = '''Что едят на полдник динозавры?
#ТиРекс-кекс!'''
#Если нужно ввести текст, занимающий несколько строк, поставьте
#в начале и в конце три одинарные кавычки.
#print(fred)
#silly_string = """Тут что-то не так, не будь я д\'Артаньян" — подумал он."""
#single_quote_str = '"Тут что-то не так, не будь я д\'Артаньян", — подумал он.'
#double_quote_str = "\"Тут что-то не так, не будь я д'Артаньян\", — подумал он."
#print(single_quote_str)
#print(double_quote_str)
#Переменные внутри строк
#myscore = 1000
#message = 'Мой счет: %s очков'
#print(message % myscore)
#joke_text = '%s: приспособление для поиска мебели в темноте'
#bodypart1 = 'Коленка'
#bodypart2 = 'Лодыжка'
#print(joke_text % bodypart1)
#print(joke_text % bodypart2)
#nums = 'Что сказало число %s числу %s? Славный поясок!'
#print(nums % (0, 8))
#Умножение строк
#print(10 * 'a')
#spaces = ' ' * 25
#print('%s Задний переулок 12' % spaces)
#print('%s Трясогузочья пустошь' % spaces)
#print('%s Западный Всхрапшир' % spaces)
#print()
#print()
#print('Уважаемый Сэр,')
#print()
#print('Хочу сообщить вам, что кое-где на крыше уборной')
#print('недостает кусков черепицы.')
#print('Думаю, прошлой ночью их сдуло внезапным порывом ветра.')
#print()
#print('С почтением')
#print('Малькольм Конфузли')
#print(1000 * 'слякоть')
#Списки мощнее строк
#wizard_list = 'Паучьи лапки, жабий палец, глаз тритона, крыло летучей мыши, жир слизня, перхоть змеи'
#print(wizard_list)
#wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
#print(wizard_list[2])
#wizard_list[2] = 'язык улитки'
#print(wizard_list)
#some_numbers = [1, 2, 5, 10, 20]
#some_strings = ['Нож', 'отточен', 'точен', 'очень']
#numbers_and_strings = [7, 'раз', 'отпей', 1, 'раз', 'отъешь']
#print(numbers_and_strings)
#numbers = [1, 2, 3, 4, 5]
#strings = ['хватит', 'циферки', 'считать']
#mylist = [numbers, strings]
#print(mylist)
#Добавление элементов в список
#wizard_list.append('медвежий коготь')
#print(wizard_list)
#wizard_list.append('мандрагора')
#wizard_list.append('болиголов')
#wizard_list.append('болотный газ')
#print(wizard_list)
#Удаление элементов из списка
#del wizard_list[5]
#print(wizard_list)
#del wizard_list[8]
#del wizard_list[7]
#del wizard_list[6]
#print(wizard_list)
#Списковая арифметика
#list1 = [1, 2, 3, 4, 5]
#list2 = ['я', 'забрался', 'под', 'кровать']
#print(list1 + list2)
#list1 = [1, 2, 3, 4]
#list2 = ['я', 'мечтаю', 'о', 'пломбире']
#list3 = list1 + list2
#print(list3)
#list1 = [1, 2]
#print(list1 * 5)
#Кортежи
#fibs = (0, 1, 1, 2, 3)
#print(fibs[3])
#Словари
#favorite_sports = ['Ральф Уильямс, Футбол',
#                   'Майкл Типпетт, Баскетбол',
#                   'Эдвард Элгар, Бейсбол',
#                   'Ребекка Кларк, Нетбол',
#                   'Этель Смит, Бадминтон',
#                   'Фрэнк Бридж, Регби']
#favorite_sports = {'Ральф Уильямс': 'Футбол',
#                   'Майкл Типпетт': 'Баскетбол',
#                   'Эдвард Элгар': 'Бейсбол',
#                   'Ребекка Кларк': 'Нетбол',
#                   'Этель Смит': 'Бадминтон',
#                   'Фрэнк Бридж': 'Регби'}
#print(favorite_sports['Ребекка Кларк'])
#del favorite_sports['Этель Смит']
#print(favorite_sports)
#favorite_sports['Ральф Уильямс'] = 'Хоккей на льду'
#print(favorite_sports)
