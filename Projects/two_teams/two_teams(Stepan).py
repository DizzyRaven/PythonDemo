def two_teams(sailors):
    list_1 = [[], []]
    for i in sailors.keys():
        if sailors[i] > 40 or sailors[i] < 20:
            list_1[0].append(i)
        else:
            list_1[1].append(i)
    for i in list_1:
        i.sort()
    return list_1

print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))