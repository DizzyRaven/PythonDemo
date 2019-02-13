def password_validate(text):
    lett_l = 0
    lett_u = 0
    numb = 0
    symb = 0
    symb_ = '$#@&'
    le = 8
    for i in text:
        if i.isalpha() and i.isupper():
            lett_u += 1
    for i in text:
        if i.isalpha() and i.islower():
            lett_l += 1
    for i in text:
        if i.isdigit():
            numb += 1
    for i in text:
        t = i in symb_
        if t == True:
            symb += 1
    if lett_l >= 1 and numb >= 1 and lett_u >= 1 and symb >= 1 and le >= 8:
        print(symb, lett_l, lett_u, numb)
        return True
    else:
        return False
assert password_validate('AA#a4568')
assert password_validate('AA&a4568')
assert not password_validate('AA#14568')
assert not password_validate('Aa#4568')
assert not password_validate('Aa114568')
assert not password_validate('AA114568')

