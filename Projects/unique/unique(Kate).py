def unique(s):
    y = []
    for i in s:
        if s.count(i) == 1:
            y.append(i)
    print(y)
    return y



assert unique('abcd') == ['a', 'b', 'c', 'd']
assert unique([1, 2, 3, 4, 1, 2, 3]) == [4]
