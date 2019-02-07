def slov(a):
    s = {}
    if a > 0:
        for i in range(0, a + 1):
            s[i] = i ** 2
    if a < 0:
        for i in range(0, abs(a) + 1):
            s[-i] = i ** 2
    print(s)

slov(-5)
