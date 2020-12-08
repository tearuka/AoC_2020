#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_02.txt").read().splitlines()


### Part 1

import re
counter = 0
for line in inp:
    mini, maxi, letter, string = re.split('-|: | ',line)
    count = string.count(letter)
    counter += int(mini) <= count <= int(maxi)

print('Result for part 1: ', counter)  # 628


### Part 2

counter = 0
for line in inp:
    pos1, pos2, letter, string = re.split('-|: | ',line)
    if (string[int(pos1) - 1] == letter) ^ (string[int(pos2) - 1] == letter):
        counter += 1

print('Result for part 2: ', counter)  # 705
