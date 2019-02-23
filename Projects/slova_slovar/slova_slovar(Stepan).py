def letter_counter(text_string):
    """Returns dict with letters and number of times each was found in text_string"""
    res_dict = {}
    text_string = text_string.lower()
    for i in text_string:
        if i.isalpha():#Возвращает True(если бувы) or False(если хоть одна не буква)
            res_dict[i] = text_string.count(i,0,len(text_string))
    return res_dict
assert letter_counter('hello!') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
assert letter_counter('Willy Wonka') == {'a': 1, 'i': 1, 'k': 1, 'l': 2, 'n': 1, 'o': 1, 'w': 2, 'y': 1}
