#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_01.txt").read().splitlines()
inp = [int(i) for i in inp]


### Part 1

for number in inp:
    diff = 2020 - number
    if(diff in inp):
        res1 = number * diff

print("Result for part 1: ", res1)  # 545379


### Part 2

for number in inp:
    diff = 2020 - number
    for x in inp:
        diff2 = diff - x
        if diff2 in inp:
            res2 = number * x * diff2

print("Result for part 2: ", res2)  # 257778836

