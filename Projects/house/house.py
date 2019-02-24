def house(plan):
    plan = plan.split('\n')
    if plan[0] == '':
        del plan[0]
    if plan[-1] == '':
        del plan[-1]
    for i in plan:
        a = i.find('#')
        b = i.rfind('#') + 1

        max_w = a - b
        return max_w
    return print(plan, )

house('''
0000000
##00##0
######0
##00##0
#0000#0
''')

"""assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

assert house('''0000
0000
#000
''') == 1

assert house('''0000
0000
''') == 0

assert house('''
0##0
0000
#00#
''') == 12"""