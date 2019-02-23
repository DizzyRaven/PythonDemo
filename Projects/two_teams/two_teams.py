def two_teams(sailors):
    f_sh = []
    s_sh = []
    for i in sailors.keys():
        if sailors[i] > 40 or sailors[i] < 20:
            f_sh.append(i)
        if sailors[i] >= 20 and sailors[i] <= 40:
            s_sh.append(i)
    f_sh.sort()
    s_sh.sort()
    return [f_sh, s_sh]
print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))


assert two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}) == [['Abrahams', 'Coleman'], ['Smith', 'Wesson']]
assert two_teams({'Fernandes': 18, 'Johnson': 22, 'Kale': 41, 'McCortney': 54}) == [['Fernandes', 'Kale', 'McCortney'], ['Johnson']]