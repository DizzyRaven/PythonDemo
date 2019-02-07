class NOD():
    def __init__(self, a, b):
        self.max_n = max(a, b)
        self.min_n = min(a, b)
    def nod_f(self):
        r = []
        sch = 0
        nod = self.min_n
        if nod == 0:
            print(self.max_n)
            return self.max_n
        while sch < self.min_n:
            x_1 = self.min_n % nod
            x_2 = self.max_n % nod
            if x_1 == 0 and x_2 == 0:
                r.append(nod)
                sch += 1
                nod -= 1
            else:
                sch += 1
                nod -= 1
        res = max(r)
        print(res)
        return(res)
        
                
a = NOD(18, 36)
a.nod_f()

"""assert NOD(24, 300) == 12
assert NOD(12, 12) == 12
assert NOD(0, 6) == 6
assert NOD(18, 36) == 18
"""
