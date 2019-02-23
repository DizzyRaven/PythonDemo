import string
def is_stressful(subj):
    if subj.isupper():
        return True
    if subj.endswith('!!!'):
        return True
    for i in subj:
        if i in string.punctuation:
            subj = subj.replace(i, '')
    subj = subj.lower()
    subj = subj.split()
    alert = ['help', 'asap', 'urgent']
    c_w = ''
    for i in subj:
        if i in alert:
            return True
        for x in i:
            if x not in c_w:
                c_w += x
        if c_w in alert:
            return True
        c_w = ''
    return False


assert is_stressful("Hi") == False
assert is_stressful("I neeed HELP") == True
assert is_stressful("We need you A.S.A.P.!!") == True