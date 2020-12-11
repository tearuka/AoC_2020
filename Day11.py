#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_11.txt").read().splitlines()
inp = [list(line) for line in inp ]

xmin, xmax = 0, len(inp[0])
ymin, ymax = 0, len(inp)


### Part 1

def check_adjacent(data, x, y):
    xleft, xright = x - 1, x + 1
    ydown, yup = y + 1, y - 1
    counter = 0
    if xleft >= xmin and yup >= ymin:
        counter += data[yup][xleft] == '#'
    if xleft >= xmin:
        counter += data[y][xleft] == '#'
    if xleft >= xmin and ydown < ymax:
        counter += data[ydown][xleft] == '#'
    if yup >= ymin:
        counter += data[yup][x] == '#'
    if ydown < ymax:
        counter += data[ydown][x] == '#'
    if xright < xmax and yup >= ymin:
        counter += data[yup][xright] == '#'
    if xright < xmax:
        counter += data[y][xright] == '#'
    if xright < xmax and ydown < ymax:
        counter += data[ydown][xright] == '#'
    return counter


import copy

def seat_patterns(data):
    data_new = copy.deepcopy(data)
    for x in range(xmax):
        for y in range(ymax):
            if data[y][x] == '#':
                seats = check_adjacent(data, x, y)
                if seats >= 4:
                    data_new[y][x] = 'L'
            elif data[y][x] == 'L':
                seats = check_adjacent(data, x, y)
                if seats == 0:
                     data_new[y][x] = '#'
    return(data_new)

def compute_occupied(data):
    occupied_seats = 0
    for x in range(xmax):
        for y in range(ymax):
            occupied_seats += data[y][x] == '#'
    return occupied_seats


data = []
data_new = inp
while data_new != data: 
    data = data_new
    data_new = seat_patterns(data)

res1 = compute_occupied(data_new)

print('Result for part 1: ', res1)  # 2166

### Part 2


def find_seat(data, x, y, direction):
    if direction == 'east':
        while x + 1 < xmax:
            if data[y][x + 1] == '#':
                return 1
            elif data[y][x + 1] == 'L':
                return 0
            x += 1
    elif direction == 'west':
        while x - 1 >= xmin:
            if data[y][x - 1] == '#':
                return 1
            elif data[y][x - 1] == 'L':
                return 0
            x -= 1
    elif direction == 'north':
        while y - 1 >= ymin:
            if data[y - 1][x] == '#':
                return 1
            elif data[y - 1][x] == 'L':
                return 0
            y -= 1
    elif direction == 'south':
        while y + 1 < ymax:
            if data[y + 1][x] == '#':
                return 1
            elif data[y + 1][x] == 'L':
                return 0
            y += 1
    elif direction == 'northwest':
        while y - 1 >= ymin and x - 1 >= xmin:
            if data[y - 1][x - 1] == '#':
                return 1
            elif data[y - 1][x - 1] == 'L':
                return 0
            x -= 1
            y -= 1
    elif direction == 'northeast':
        while y - 1 >= ymin and x + 1 < xmax:
            if data[y - 1][x + 1] == '#':
                return 1
            elif data[y - 1][x + 1] == 'L':
                return 0
            x += 1
            y -= 1
    elif direction == 'southwest':
        while y + 1 < ymax and x - 1 >= xmin:
            if data[y + 1][x - 1] == '#':
                return 1
            elif data[y + 1][x - 1] == 'L':
                return 0
            x -= 1
            y += 1
    elif direction == 'southeast':
        while y + 1 < ymax and x + 1 < xmax:
            if data[y + 1][x + 1] == '#':
                return 1
            elif data[y + 1][x + 1] == 'L':
                return 0
            x += 1
            y += 1
    return 0


def find_seat_sum(data, x, y):
    r1 = find_seat(data, x, y, 'east')
    r2 = find_seat(data, x, y, 'west')
    r3 = find_seat(data, x, y, 'north')
    r4 = find_seat(data, x, y, 'south')
    r5 = find_seat(data, x, y, 'northwest')
    r6 = find_seat(data, x, y, 'northeast')
    r7 = find_seat(data, x, y, 'southwest')
    r8 = find_seat(data, x, y, 'southeast')
    suma = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
    return suma


def seat_patterns_diagonals(data):
    data_new = copy.deepcopy(data)
    for x in range(xmax):
        for y in range(ymax):
            if data[y][x] == '#':
                seats = find_seat_sum(data, x, y)
                if seats >= 5:
                    data_new[y][x] = 'L'
            elif data[y][x] == 'L':
                seats = find_seat_sum(data, x, y)
                if seats == 0:
                     data_new[y][x] = '#'
    return(data_new)


data = []
data_new = inp
while data_new != data: 
    data = data_new
    data_new = seat_patterns_diagonals(data)

res2 = compute_occupied(data_new)

print('Result for part 2: ', res2)  # 1955
