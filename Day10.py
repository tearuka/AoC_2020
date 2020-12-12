#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_10.txt").read().splitlines()
inp = [int(line) for line in inp]


### Part 1

adapters = sorted(inp)
# add charging outlet at the beginning
adapters.insert(0, 0)
# add built-in adapter at the end
adapters.append(max(inp) + 3)

def check_adapters(data):
    pos = 0
    count1, count3 = 0, 0
    where_to_cut = [0]
    for pos in range(len(adapters) - 1):
        difference = adapters[pos + 1] - adapters[pos]
        count1 += difference == 1
        count3 += difference == 3
        pos += 1
        # find differences of three to know where to cut list
        if difference == 3:
            where_to_cut.append(pos)
    res1 = count1 * count3
    return res1, where_to_cut

res1, cut_positions = check_adapters(adapters)

print('Result for part 1: ', res1)  # 1998


### Part 2

# number of combinations depending on sublist length {sublist length : number of possible combinations}
dict_combo = {1:1, 2:1, 3:2, 4:4, 5:7, 6:13}

def find_combinations(data, where_to_cut):
    combos = 1
    for pos in range(len(where_to_cut) - 1):
        lst = data[cut_positions[pos] : cut_positions[pos + 1]]
        combos *= dict_combo[len(lst)]
    return combos

res2 = find_combinations(adapters, cut_positions)

print('Result for part 2: ', res2)  # 347250213298688

