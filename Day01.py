#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_01.txt").read().splitlines()

# convert it to integer
inp = [int(i) for i in inp]


### Part 1

for number in inp:
    diff = 2020 - number
    if(diff in inp):
        result = number * diff
print(result)


### Part 2

for number in inp:
    diff = 2020 - number
    for x in inp:
        diff2 = diff - x
        if(diff2 in inp):
            result = number * x * diff2
print(result)

