#O (N**2)
'''def strcounter(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(f'{sym} - {counter}')'''

# O (2 * N) = O (N), т.к. 2 - const, ей можно принебречь
'''def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) +1
    for sym, counter in syms_counter.items():
        print(f'{sym} - {counter}')'''

def strcounter(s):
    for sym in set(s):
        print(f'{sym} - {s.count(sym)}')
