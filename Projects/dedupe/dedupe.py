def dedupe(a):
    s = {}
    for i in a:
        s[i] = 1
    l = s.keys()
    l = list(l)
    return l

a = [1,2,3,4,3,2,1]
print(dedupe(a))

