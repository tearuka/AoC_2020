#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_05.txt").read().splitlines()


### Part 1

def find_row(string):
    val_min = 0
    val_max = 128
    for i in range(7):
        if string[i] == 'F':
            val_min = val_min
            val_max = (val_max + val_min - 1)//2
        elif string[i] == 'B':
            val_min = (val_max + val_min + 1)//2
            val_max = val_max
    return(val_min)

def find_column(string):
    val_min = 0
    val_max = 8
    for i in range(3):
        if string[i + 7] == 'L':
            val_min = val_min
            val_max = (val_max + val_min - 1)//2
        elif string[i + 7] == 'R':
            val_min = (val_max + val_min + 1)//2
            val_max = val_max
    return(val_min)

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

# sort ascending
IDs_sorted = sorted(IDs)

# find missing value in list
def find_missing(lst):
    missing_value = [x for x in range(lst[0], lst[-1] + 1) if x not in lst]
    return(missing_value)

my_seat = find_missing(IDs_sorted)

print("Result for part 2: ", my_seat[0])

