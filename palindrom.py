word = []
def palindrom_check(s):
    for sym in s:
        word.append(sym)
    word_reverse = word[::-1]
    if word == word_reverse:
        print('True')
    else:
        print('False')
palindrom_check('шогогош')