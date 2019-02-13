def nod(a, b):
    while a != b:
        if a > b:
            a = a - b
        if b > a:
            b = b - a
    print(a)


nod(24, 300)
