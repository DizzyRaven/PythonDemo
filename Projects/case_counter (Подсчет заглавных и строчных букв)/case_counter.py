def case_counter(a):
    u = 0
    l = 0
    for i in a:
        if i.isalpha() and i.isupper():
            u += 1
        if i.isalpha() and i.islower():
            l += 1
    res = (l, u)
    print(res)
    return res

assert case_counter('Hello!') == (4, 1)
assert case_counter('Hello World!') == (8, 2)
