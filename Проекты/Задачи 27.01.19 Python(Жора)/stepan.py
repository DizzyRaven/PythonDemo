import string
from time import time,sleep
# all letters: string.ascii_letters
# all punctuation symbols: string.punctuation
# all whitespace symbols: string.whitespace
start = time()
def word_letter_counter(text_string):
    sleep(1)
    """Returns tuple with number of letters and number of words in text_string."""
    letters = 0
    words = 0
    whitespace = 0
    def text_red(text_new):
        result = text_new
        for i in text_new:
            if i in string.punctuation:
                result = text_new.replace(i, "")
        return result
    result = text_red(text_string) + " "
    for i in result:
        if i in string.ascii_letters:
            letters += 1
            whitespace = 0
        elif i in string.punctuation:
            words += 1
        elif i in string.whitespace:
            whitespace += 1
            if whitespace > 1:
                continue
            words += 1
    return letters, words
print(word_letter_counter("Hi\tThere\n"))
end = time()
print(end-start)
