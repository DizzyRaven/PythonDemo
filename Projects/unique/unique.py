def unique(b):
    a = {}
    f = []
    for i in b:
        a[i] = b.count(i)#, 0, len(b))
        if a[i] == 1:
            f.append(i)
    print(f)
    return f

assert unique('abcd') == ['a', 'b', 'c', 'd']
assert unique([1, 2, 3, 4, 1, 2, 3]) == [4]
