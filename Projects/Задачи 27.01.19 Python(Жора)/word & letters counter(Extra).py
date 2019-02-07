import string
from time import time,sleep
def word_letter_counter(a):
    s = a.rsplit(sep=None, maxsplit=-1)
    w = len(s)
    l = 0
    for i in a:
        tf = i in string.ascii_letters
        if tf == True:
            l += 1
    return(l, w)
    print(l, w)
print(word_letter_counter("Hi\tThere\n"))

"""assert word_letter_counter('hello') == (5, 1)
assert word_letter_counter('hello World!') == (10, 2)
assert word_letter_counter('Hi\tThere') == (7, 2)
assert word_letter_counter('Hi\tThere\n') == (7, 2)"""
