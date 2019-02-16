def reverse(x):
    l = x.split(' ')
    l.reverse()
    t = ' '.join(l)
    print(t)
    return t




    
s = "My name is Nik"
reverse(s)
assert reverse(s) == "Nik is name My"
