#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_09.txt").read().splitlines()
inp = [int(line) for line in inp]


### Part 1

def is_sum(data, objective, preamble):
    counter = 0
    for num in data:
        difference = objective - num
        if difference not in data:
            counter += 1
    if counter < preamble:
        return(0)
    else:
        return(1)

def find_number(data, preamble):
    pos = 0
    for number in data[preamble:]:
        result = is_sum(data[pos : preamble + pos], number, preamble)
        pos += 1
        if result == 1 :
            return(number)

res1 = find_number(inp, 25)

print('Result for part 1: ', res1)  # 530627549


### Part 2

def find_list_sum(data, objective):
    for pos in range(len(data)):
        suma = 0
        lst = []
        while pos < len(data) - 1:
            suma += data[pos] 
            lst.append(data[pos])
            pos = pos + 1
            if suma == objective:
                return(min(lst) + max(lst))

res2 = find_list_sum(inp, res1)

print('Result for part 2: ', res2)  # 77730285

