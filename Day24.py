#!/usr/bin/env python
# coding: utf-8


import copy

# read input
inp = open('inp/input_24.txt').read().splitlines()

# parse input
tiles_lst = []
for string in inp:
    i = 0
    lst = []
    while i < len(string):
        if string[i] in 'ew':
            lst.append(string[i])
            i += 1
        else:
            lst.append(string[i] + string[i + 1])
            i += 2
    tiles_lst.append(lst)


### Part 1

d = {}
for line in tiles_lst:
    x, y = 0, 0
    
    for element in line:
        if element == 'e':
            x += 1
        elif element == 'se':
            if y % 2 != 0:
                x += 1
            y += 1
        elif element == 'sw': 
            if y % 2 == 0:
                x -= 1 
            y += 1
        elif element == 'w':
            x -= 1
        elif element == 'nw':
            if y % 2 == 0:
                x -= 1
            y -= 1
        elif element == 'ne':
            if y % 2 != 0:
                x += 1
            y -= 1

    if (x,y) not in d or d[x,y] == 0:
        d1 = {(x, y): 1}
    elif d[x,y] == 1:
        d1 = {(x, y): 0}
    d.update(d1)

val_list = list(d.values())
res1 = sum(val_list)

print('Result for part 1: ', res1)  # 495


### Part 2

def find_adjacent(x, y):
    hex_e = (x + 1, y)
    hex_w = (x - 1, y)
    if y % 2 == 0:
        hex_ne = (x, y - 1)
        hex_nw = (x - 1, y - 1)
        hex_se = (x, y + 1)
        hex_sw = (x - 1, y + 1)
    elif y % 2 != 0:
        hex_ne = (x + 1, y - 1)
        hex_nw = (x, y - 1)
        hex_se = (x + 1, y + 1)
        hex_sw = (x, y + 1)
    lst = [hex_e, hex_w, hex_se, hex_sw, hex_ne, hex_nw]
    return lst

def expand_neighbors(d):
    d_expanded = copy.deepcopy(d)
    for key in d:
        neighbors = find_adjacent(key[0], key[1])
        for neighbor in neighbors:
            if neighbor not in d:
                d_expanded[neighbor] = 0
    return d_expanded

def flip_tiles(d):
    d_new = copy.deepcopy(d)
    for key in d:
        neighbors = find_adjacent(key[0], key[1])
        suma = 0
        for neighbor in neighbors:    
            if neighbor in d:
                suma += d[neighbor]
        if d[key] == 1:
            if suma == 0 or suma > 2:
                d_new[key] = 0
        if d[key] == 0:
            if suma == 2:
                d_new[key] = 1
    return d_new

for _ in range(100):
    d_expanded = expand_neighbors(d)
    d_new = flip_tiles(d_expanded)
    val_list = list(d_new.values())
    res2 = sum(val_list)
    d = d_new
    
print('Result for part 2: ',res2)  # 4012

