string = "этот если способ вы плохо это подходит читаете для что-то шифрования пошло важных не сообщений так"
s = string.rsplit(sep=None, maxsplit=-1)
d = len(s)
#print(s)
#print(d)
def word_recombiner(s):
    i = list(range(0, d, 2))
    new_s = []
    for x in i:
        new_s.append(s[x])
    return new_s
    print(new_s)

