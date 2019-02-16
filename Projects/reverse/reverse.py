def reverse(s):
    new = []
    spl = s.rsplit(sep=None, maxsplit=-1)
    sch = len(spl) - 1
    while sch >= 0:
        new.append(spl[sch])
        sch -= 1
    new_1 = ' '.join(new)
    print(new_1)
s = "My name is Nik"
assert reverse(s) == "Nik is name My"