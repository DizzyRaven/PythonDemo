#Применение функций
#list(range(0, 5))
#==============================
#Строение функции
"""def testfunc(myname):
    print("Привет, %s" % myname)"""
#==============================
"""fname = "Kate"
lname = "Varzaba"
def testfunc(fname, lname):
    print("Привет, %s %s" % (fname, lname))"""
#==============================
"""def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending"""
#=====================================================================
#Переменные и область видимости
"""def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable"""
#==============================
"""another_variable = 100
def variable_test2():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable"""
#==============================
"""def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans += cans
        print('Неделя %s, банок: %s' % (week, total_cans))"""
#==============================
#Применение модулей
"""import time
a = time.asctime()
print(a)"""
#==============================
""""import sys
a = 1707
print(a)
a = sys.stdin.readline()
print(a)"""
#==============================
"""import sys
def saj():
    print('Сколько вам лет?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
    else:
        print('Что-что?')"""
#==============================
