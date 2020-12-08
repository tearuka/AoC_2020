#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_03.txt").read().splitlines()


### Part 1

# define function for grid expansion
def expand_grid(data, step_x_max):
    expand_times = round(step_x_max * (len(data) - 1) / len(data[0])) + 1
    data_big = [data[i] * expand_times for i in range(len(data))]
    return(data_big)

# define function for sliding with a toboggan
def toboggan(data, step_x, step_y):
    x = 0
    y = 0
    trees = 0
    for step in range((len(data) - 1) // step_y):
        x = x + step_x
        y = y + step_y
        value = data[y][x]
        trees += value == '#'
    return(trees)

inp_big = expand_grid(inp, 3)
result_part1 = toboggan(inp_big, 3, 1)

print("Result for part 1: ", result_part1)  # 145


### Part 2

inp_bigg = expand_grid(inp, 7)
res1 = toboggan(inp_bigg, 1, 1)
res2 = toboggan(inp_bigg, 3, 1)
res3 = toboggan(inp_bigg, 5, 1)
res4 = toboggan(inp_bigg, 7, 1)
res5 = toboggan(inp_bigg, 1, 2)

result_part2 = res1 * res2 * res3 * res4 * res5

print("Result for part 2: ", result_part2)  # 3424528800
