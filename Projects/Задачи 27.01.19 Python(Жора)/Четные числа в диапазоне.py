def find_even(mi, ma):
    s = []
    for i in range(mi, ma + 1):
        if i % 2 == 0:
            s.append(i)
    return(s)
    print(s)
