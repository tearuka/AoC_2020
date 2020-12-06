#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_06.txt").read().split("\n\n")


### Part 1

# put each line in one big string
inp_all = [line.replace('\n','') for line in inp]

count_unique = 0
for line in inp_all:
    count_unique += len(set(line))

print("Result for part 1: ", count_unique)


### Part 2

# split input by \n
inp_sep = [line.split('\n') for line in inp]

count_intersect = 0
for line in inp_sep:
    lst = []
    for string in line:
        # create a list of sets
        lst.append(set(string))
    # intersect a list of sets
    matching = lst[0].intersection(*lst)
    count_intersect += len(matching)

print("Result for part 2: ", count_intersect)