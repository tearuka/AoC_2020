#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_02.txt").read().splitlines()


### Part 1

import re
counter = 0
for line in inp:
    split_text = re.split('-|: | ',line)
    mini = int(split_text[0])
    maxi = int(split_text[1])
    letter = split_text[2]
    string = split_text[3]
    count = string.count(letter)
    if count >= mini and count <= maxi:
        counter = counter + 1
print(counter)


### Part 2

counter = 0
for line in inp:
    split_text = re.split('-|: | ',line)
    pos1 = int(split_text[0])
    pos2 = int(split_text[1])
    letter = split_text[2]
    string = split_text[3]
    if (string[pos1 - 1] == letter and string[pos2 - 1] != letter) or (string[pos1 - 1] != letter and string[pos2 - 1] == letter):
        counter = counter + 1
print(counter)

