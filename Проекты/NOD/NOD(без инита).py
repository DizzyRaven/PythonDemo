def nod_f(a, b):
    max_n = max(a, b)
    min_n = min(a, b)
    r = []
    sch = 0
    nod = min_n
    if nod == 0:
        #print(max_n)
        return max_n
    while sch < min_n:
        x_1 = min_n % nod
        x_2 = max_n % nod
        if x_1 == 0 and x_2 == 0:
            r.append(nod)
            sch += 1
            nod -= 1
        else:
            sch += 1
            nod -= 1
    res = max(r)
    #print(res)
    return(res)
        

assert nod_f(24, 300) == 12
assert nod_f(12, 12) == 12
assert nod_f(0, 6) == 6
assert nod_f(18, 36) == 18

