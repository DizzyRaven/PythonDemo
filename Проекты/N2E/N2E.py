name = input('Введите Имя лида: ')
surname = input('Введите Фамилию лида: ')
domain = input('Введите Домен: ')
form = input('Введите номер формы(максимальный номер - 34): ')
'''s - это словарь с вариациями комбинаций
       имени, фамилии и, иногда, разделителя, где
       ключем выступают цифры от 1 до 34'''
s = {
    1 : name + '@' + domain,
    2 : surname + '@' + domain,
    3 : name + surname + '@' + domain,
    4 : name + '.' + surname + '@' + domain,
    5 : name[0] + surname + '@' + domain,
    6 : name[0] + '.' + surname + '@' + domain,
    7 : name + surname[0] + '@' + domain,
    8 : name + '.' + surname[0] + '@' + domain,
    9 : name[0] + surname[0] + '@' + domain,
    10 : name[0] + '.' + surname[0] + '@' + domain,
    11 : surname + name + '@' + domain,
    12 : surname + '.' + name + '@' + domain,
    13 : surname + name[0] + '@' + domain,
    14 : surname + '.' + name[0] + '@' + domain,
    15 : surname[0] + name + '@' + domain,
    16 : surname[0] + '.' + name + '@' + domain,
    17 : surname[0] + name[0] + '@' + domain,
    18 : surname[0] + '.' + name[0] + '@' + domain,
    19 : name + '-' + surname + '@' + domain,
    20 : name[0] + '-' + surname + '@' + domain,
    21 : name + '-' + surname[0] + '@' + domain,
    22 : name[0] + '-' + surname[0] + '@' + domain,
    23 : surname + '-' + name + '@' + domain,
    24 : surname + '-' + name[0] + '@' + domain,
    25 : surname[0] + '-' + name + '@' + domain,
    26 : surname[0] + '-' + name[0] + '@' + domain,
    27 : name + '_' + surname + '@' + domain,
    28 : name[0] + '_' + surname + '@' + domain,
    29 : name + '_' + surname[0] + '@' + domain,
    30 : name[0] + '_' + surname[0] + '@' + domain,
    31 : surname + '_' + name + '@' + domain,
    32 : surname + '_' + name[0] + '@' + domain,
    33 : surname[0] + '_' + name + '@' + domain,
    34 : surname[0] + '_' + name[0] + '@' + domain,
}

'''тут мы выводим на экран нужный нам вариант эмейла, 
   определяя ключ к словарю (с вариациями s) тот номер, 
   котоый мы вводили в начале, предварительно переведя 
   его в числовой тип данных.'''

print(s[int(form)])


