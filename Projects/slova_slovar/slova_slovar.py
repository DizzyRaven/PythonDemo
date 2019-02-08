import string
def slova_slovar(data):
    s = {}
    for i in data:
        p = i in string.ascii_letters
        if p == True:
            s[i.lower()] = 1
    l = s.keys()
    l = list(l)
    l.sort()
    s2 = {}
    for i in l:
        s = i
        s2[s] = 0
        for i2 in data:
            if s == i2.lower():
                s2[s.lower()] += 1
    print(s2)
    return(s2)

assert slova_slovar('hello!') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
assert slova_slovar('Willy Wonka') == {'a': 1, 'i': 1, 'k': 1, 'l': 2, 'n': 1, 'o': 1, 'w': 2, 'y': 1}
