#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_05.txt").read().splitlines()


### Part 1

def find_value(string, val_min, val_max):
    for c in string:
        if c in 'FL':
            val_max = (val_max + val_min) // 2
        elif c in 'BR':
            val_min = (val_max + val_min) // 2
    return val_min

def find_row(string):
    return find_value(string[:7], 0, 128)
    
def find_column(string):
    return find_value(string[7:], 0, 8)

# find highest seat ID 
maxi = 0
for line in inp:
    row = find_row(line)
    column = find_column(line)
    seat_ID = row * 8 + column
    if seat_ID > maxi:
        maxi = seat_ID

print("Result for part 1: ", maxi)


### Part 2

# create a list of all seat IDs
IDs = []
for line in inp:
    row = find_row(line)
    column = find_column(line)
    seat_ID = row * 8 + column
    IDs.append(seat_ID)

def find_missing(lst):
    for x in range(min(lst),max(lst)):
        if x not in lst:
            return x

my_seat = find_missing(IDs)

print("Result for part 2: ", my_seat)

