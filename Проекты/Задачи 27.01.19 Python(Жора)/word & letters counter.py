import string
from time import time,sleep
start = time()
def word_letter_counter(a):
    sleep(1)
    l = 0
    w = 0
    word = False
    a = a + ' '
    for i in a:
        tf = i in string.ascii_letters
        tf_01 = i in string.whitespace
        if tf == True:
            l += 1
            word = True
        elif tf_01 == True and word == True:
            w += 1
            word = False  
    return(l, w)
    print(l, w)
print(word_letter_counter("Hi\tThere\n"))
end = time()
print(end-start)
"""assert word_letter_counter('hello') == (5, 1)
assert word_letter_counter('hello World!') == (10, 2)
assert word_letter_counter('Hi\tThere') == (7, 2)
assert word_letter_counter('Hi\tThere\n') == (7, 2)"""
