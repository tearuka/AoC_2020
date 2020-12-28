#!/usr/bin/env python
# coding: utf-8


# input
inp = [3, 6, 4, 2, 9, 7, 5, 8, 1]


### Part 1

cups = inp.copy()

maxi = max(cups)
for step in range(1000):
    current_cup = cups[0]
    pick_up = cups[1 : 4]
    destination_cup = current_cup - 1
    while destination_cup in pick_up or destination_cup == 0:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = maxi
    index = cups.index(destination_cup)
    cups = cups[4:index + 1] + pick_up + cups[index + 1 :] + [cups[0]]

index = cups.index(1)
lst_res = cups[index + 1:] + cups[:index]
lst_res = [str(num) for num in lst_res]
res1 = int(''.join(lst_res))

print('Result for part 1: ', res1)  # 24786953


### Part 2

num_cups = 1000000
num_steps = 10000000
cups = inp.copy()
cups = cups + list(range(10, num_cups + 1))


# 'linked list'-like code adapted from reddit user imbadatreading --> thanks a lot!
def solve(num_cups):
    d = [0] * num_steps
    for i in range(len(cups)):
        if i == len(cups) - 1:
            d[cups[i]] = cups[0]
        else:
            d[cups[i]] = cups[i+1]

    current_cup = cups[0]
    for i in range(num_steps + 1):
        a = d[current_cup]
        b = d[a]
        c = d[b]
        d[current_cup] = d[c]
        destination_cup = current_cup - 1
        
        while destination_cup in [a,b,c] or destination_cup == 0:
            destination_cup -=1
            if destination_cup < 1:
                destination_cup = num_cups
        d[c] = d[destination_cup]
        d[destination_cup] = a
        current_cup = d[current_cup]

    return d[1] * d[d[1]]


res2 = solve(num_cups)

print('Result for part 2: ', res2)  # 42271866720






