#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_08.txt").read().splitlines()
inp = [line.split(' ') for line in inp]


### Part 1

def run_instructions(data):
    pointer = 0
    accumulator = 0
    positions_visited = []
    while pointer not in positions_visited:
        if pointer > len(data) - 1:
            print('Result for part 2: ', accumulator)
            return(accumulator)
        positions_visited.append(pointer)
        operation = data[pointer][0]
        num = int(data[pointer][1])
        if operation == 'acc':
            accumulator += num
            pointer += 1
        elif operation == 'jmp':
            pointer += num
        elif operation == 'nop':
            pointer += 1
    return(accumulator)

print('Result for part 1: ', run_instructions(inp))  # 1797


### Part 2

indices_all = [i for i, line in enumerate(inp) if line[0] == 'nop' or line[0] == 'jmp']

import copy
for index in indices_all:
    data_changed = copy.deepcopy(inp)
    if data_changed[index][0] == 'jmp':
        data_changed[index][0] = 'nop'
    elif data_changed[index][0] == 'nop':
        data_changed[index][0] = 'jmp'
    run_instructions(data_changed)
 
# Result for part 2: 1036
