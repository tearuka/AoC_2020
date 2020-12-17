#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_14.txt").read()

# I want to get the following format:
# masks = ['001X11X1X010X1X1010XX10X100101011000', 'X0100001101XX11100010XX110XX11111000']
# memory_addresses = [[43398, 51673, 18028], [24151, 15368, 45005, 1842, 36033, 26874]]
# decimal_numbers = [[563312, 263978, 544304215], [2013, 19793, 478, 190808161, 987, 102]]

# parse input
inp_split = inp.split('mask = ')
inp_split = [line[:-1] for line in inp_split]
inp_split = inp_split[1:]
inp_split = [line.split('\nmem[') for line in inp_split]

# divide into two parts
masks = [line[0] for line in inp_split]
lst_without_masks = [line[1:] for line in inp_split]

# make lists for memory addresses and decimal numbers for each
memory_addresses = []
decimal_numbers = []
for line in lst_without_masks:
    memory_addresses_small = []
    decimal_numbers_small = []
    for i in range(len(line)):
        address, decimal_number = line[i].split('] = ')
        memory_addresses_small.append(int(address))
        decimal_numbers_small.append(int(decimal_number))
    memory_addresses.append(memory_addresses_small)
    decimal_numbers.append(decimal_numbers_small)


### Part 1

# cycle -> related to each mask
# step -> related to each memory address 

def initialize_program(masks, memory_addresses, decimal_numbers):
    initial_value = '0'*36
    d = {}
    for cycle in range(len(masks)):
        for step in range(len(memory_addresses[cycle])):
            result = list(initial_value)
            binary_number = '{0:036b}'.format(decimal_numbers[cycle][step])
            for i in range(36):
                if masks[cycle][i] == 'X':
                    result[i] = binary_number[i]
                elif masks[cycle][i] in ('1','0'):
                    result[i] = masks[cycle][i]
            result_decimal = int(''.join(result),2)
            d1 = {memory_addresses[cycle][step]: result_decimal}
            d.update(d1)
    lst = list(d.values())
    return sum(lst)

res1 = initialize_program(masks, memory_addresses, decimal_numbers)
print('Result for part 1: ', res1)  # 6317049172545


### Part 2

from itertools import product

def decoder_chip(masks, memory_addresses, decimal_numbers):
    initial_value = '0'*36
    d = {}
    for cycle in range(len(masks)):
        for step in range(len(memory_addresses[cycle])):
            result = list(initial_value)
            address_binary = '{0:036b}'.format(memory_addresses[cycle][step])
            countX = 0
            lst_posX = []
            for i in range(36):
                if masks[cycle][i] == '0':
                    result[i] = address_binary[i]
                elif masks[cycle][i] == '1':
                    result[i] = '1'
                elif masks[cycle][i] == 'X':
                    result[i] = 'X'
                    countX += 1
                    lst_posX.append(i)
            combos = list(product(range(2), repeat = countX))
            for combo in combos:
                for j in range(len(lst_posX)):
                    result[lst_posX[j]] = str(combo[j])
                address_decimal = int(''.join(result),2)
                d1 = {address_decimal: decimal_numbers[cycle][step]}
                d.update(d1)
    lst = list(d.values())
    return sum(lst)

res2 = decoder_chip(masks, memory_addresses, decimal_numbers)
print('Result for part 2: ', res2)  # 3434009980379
