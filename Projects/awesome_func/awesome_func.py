max_val = 10
awesome_gen = filter(lambda val: bool(val % 2), map(lambda x: pow(x, 2.2), [idx for idx in range(1, max_val)]))


def awesome_func(max_val):
    s = [pow(i, 2.2) for i in range(1, max_val)]
    s_1 = []
    for i in s:
        if i % 2 != 0:
            s_1.append(i)
    for i in s_1:
        yield i
assert list(awesome_gen) == list(awesome_func(max_val))