#!/usr/bin/env python
# coding: utf-8


# read input
inp = open('inp/input_17.txt').read().splitlines()

# create dictionaries 
inp_3D = {}
for y in range(len(inp)):
    for x in range(len(inp[0])):
        inp_3D[y, x, 0] = inp[y][x]        

inp_4D = {}
for y in range(len(inp)):
    for x in range(len(inp[0])):
        inp_4D[y, x, 0, 0] = inp[y][x]


### Part 1

from itertools import product

def get_neighbors_3D(x, y, z):
    neighbors = list(product([x - 1, x, x + 1],[y - 1, y, y + 1],[z - 1, z, z + 1]))
    neighbors.remove((x, y, z))
    return neighbors


import copy

def check_adjacent_3D(data):
    data_new = copy.deepcopy(data)
    for z in range(zmin, zmax):
        for y in range(ymin, ymax):
            for x in range(xmin, xmax):
                counter = 0
                neighbors = get_neighbors_3D(x, y, z)
                for neighbor in neighbors:
                    xnb, ynb, znb = neighbor
                    if (ynb, xnb, znb) in data:
                        counter += data[ynb, xnb, znb] == '#'
                if (y, x, z) in data:
                    if data[y, x, z] == '#':
                        if counter not in (2,3):
                            data_new[y, x, z] = '.'
                    elif data[y, x, z] == '.':
                        if counter == 3:
                            data_new[y, x, z] = '#'
                else:
                    if counter == 3:
                        data_new[y, x, z] = '#'
                    else:
                        data_new[y, x, z] = '.'
    return data_new


# go through 6 cycles, while expanding the coordinates
xmin, xmax = 0 - 1, len(inp[0]) + 1
ymin, ymax = 0 - 1, len(inp) + 1
zmin, zmax = -1, 2
result_new = inp_3D
for _ in range(6):
    result = result_new
    result_new = check_adjacent_3D(result)
    xmin, xmax = xmin - 1, xmax + 1
    ymin, ymax = ymin - 1, ymax + 1
    zmin, zmax = zmin - 1, zmax + 1
total_sum = 0
for element in list(result_new.values()):
    total_sum += element == '#'

print('Result for part 1: ', total_sum)  # 319



### Part 2

def get_neighbors_4D(x, y, z, w):
    neighbors = list(product([x - 1, x, x + 1],[y - 1, y, y + 1],[z - 1, z, z + 1],[w - 1, w, w + 1]))
    neighbors.remove((x, y, z, w))
    return neighbors


def check_adjacent_4D(data):
    data_new = copy.deepcopy(data)
    for w in range(wmin, wmax):
        for z in range(zmin, zmax):
            for y in range(ymin, ymax):
                for x in range(xmin, xmax):
                    counter = 0
                    neighbors = get_neighbors_4D(x, y, z, w)
                    for neighbor in neighbors:
                        xnb, ynb, znb, wnb = neighbor
                        if (ynb, xnb, znb, wnb) in data:
                            counter += data[ynb, xnb, znb, wnb] == '#'
                    if (y, x, z, w) in data:
                        if data[y, x, z, w] == '#':
                            if counter not in (2,3):
                                data_new[y, x, z, w] = '.'
                        elif data[y, x, z, w] == '.':
                            if counter == 3:
                                data_new[y, x, z, w] = '#'
                    else:
                        if counter == 3:
                            data_new[y, x, z, w] = '#'
                        else:
                            data_new[y, x, z, w] = '.'
    return data_new


# go through 6 cycles, while expanding the coordinates
xmin, xmax = 0 - 1, len(inp[0]) + 1
ymin, ymax = 0 - 1, len(inp) + 1
zmin, zmax = -1, 2
wmin, wmax = -1, 2
result_new = inp_4D
for _ in range(6):
    result = result_new
    result_new = check_adjacent_4D(result)
    xmin, xmax = xmin - 1, xmax + 1
    ymin, ymax = ymin - 1, ymax + 1
    zmin, zmax = zmin - 1, zmax + 1
    wmin, wmax = wmin - 1, wmax + 1
total_sum = 0
for element in list(result_new.values()):
    total_sum += element == '#'

print('Result for part 2: ', total_sum)  # 2324
