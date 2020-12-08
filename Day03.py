#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_03.txt").read().splitlines()


### Part 1

def toboggan(data, step_x, step_y):
    x, y = 0, 0
    trees = 0
    while y < len(data) - 1:
        x += step_x
        y += step_y
        value = data[y][x % len(inp[0])]
        trees += value == '#'
    return(trees)

result_part1 = toboggan(inp, 3, 1)

print("Result for part 1: ", result_part1)  # 145


### Part 2

res1 = toboggan(inp, 1, 1)
res2 = toboggan(inp, 3, 1)
res3 = toboggan(inp, 5, 1)
res4 = toboggan(inp, 7, 1)
res5 = toboggan(inp, 1, 2)

result_part2 = res1 * res2 * res3 * res4 * res5

print("Result for part 2: ", result_part2)  # 3424528800
