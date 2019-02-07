def slov(x):
    s = {}
    sch = 0
    while sch <= x:
        s[sch] = sch ** 2
        sch += 1
    if sch == 0:
        while sch >= x:
            s[sch] = sch ** 2
            sch -= 1
    return s
    print(s)
slov(5)
