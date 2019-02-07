#Использование цикла for
#name = "Sergey"
#t = len(name)
#for x in range(0, t):
#    print("Привет!")
#==============================
#print(list(range(10, 21)))
#==============================
#for x in range(0, 5):
#    print("привет %s" % x)
#==============================
#wizard_list = ["паучьи лапки", "жабий палец", "язык улитки", "крыло летучей мыши", "жир слизня", "медвежий коготь"]
#for i in wizard_list:
#    print(i)
#==============================
#hugehairypants = ["огромные", "волосатые", "штаны"]
#for i in hugehairypants:
#    print(i)
#    print(i)
#==============================
#hugehairypants = ["огромные", "волосатые", "штаны"]
#for i in hugehairypants:
#    print(i)
#    for j in hugehairypants:
#        print(j)
#==============================
#found_coins = 20
#magic_coins = 70
#stolen_coins = 3
#coins = found_coins
#for week in range(1, 53):
#    coins = coins + magic_coins - stolen_coins
#    print("Неделя %s = %s" % (week, coins))
#=====================================================================
#Цикл while
#цикл while, используется если нужное количество повторов заранее
#неизвестно, тогда как for расчитан на определенное число повторов.
#for step in range(1, 21):
#    print (step)
#==============================
"""mana = 1500
goblins = 30
fb = 50
while goblins > 0:
    print("Ты убил гоблина!")
    mana = mana - fb
    goblins = goblins - 1
    print("Осталось %s Гоблинов и %s Маны" % (goblins, mana))
    if mana == 0 and goblins > 0:
        print("You are dead!")
        break
    elif goblins == 0:
        print("Ты убил всех гоблинов!")"""
#==============================
"""step = 0
while step < 10000:
    print(step)
    if tired == True:
        break
    elif badweather == True:
        break
    else:
        step = step + 1"""
#==============================
"""x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)"""
#==============================
"""while True:
    много кода
    много кода
    много кода
    if some_value == True:
        break"""
#=====================================================================
