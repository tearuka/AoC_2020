#!/usr/bin/env python
# coding: utf-8


inp = [17,1,3,16,19,0]


def memory_game(data, n_steps):
    pos = 0
    d = {}
    number_spoken = data[0]
    for _ in range(n_steps):  
        last_number_spoken = number_spoken
        if pos < len(inp):
            number_spoken = data[pos]
        elif number_spoken not in d:
            number_spoken = 0
        else:
            number_spoken = pos - 1 - d[number_spoken]
        d1 = {last_number_spoken: pos - 1}
        d.update(d1)
        pos += 1
    return(number_spoken)


res1 = memory_game(inp, 2020)
print('Result for part 1: ', res1)  # 694

res2 = memory_game(inp, 30000000)
print('Result for part 2: ', res2)  # 21768614

