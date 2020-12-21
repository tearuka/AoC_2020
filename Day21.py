#!/usr/bin/env python
# coding: utf-8


# read input
inp = open('inp/input_21.txt').read().splitlines()
inp = [line.split(' (contains ') for line in inp]

# parse input
ingredients = [line[0] for line in inp]
ingredients = [line.split(' ') for line in ingredients]
allergens = [line[1] for line in inp]
allergens = [line[:-1] for line in allergens]
allergens = [line.split(', ') for line in allergens]


### Part 1

def find_allergens(ingredients, allergens):
    d = {}
    for i in range(len(allergens)):
        for allergen in allergens[i]:
            if allergen not in d:
                d1 = {allergen: ingredients[i]}
            else:
                intersection = set(d[allergen]).intersection(ingredients[i])
                d1 = {allergen: intersection}
            d.update(d1)
    return d

d_allergens = find_allergens(ingredients, allergens)

val_list = list(d_allergens.values())
chosen_ones = sorted(set([item for sublist in val_list for item in sublist]))

counter = 0
for lst in ingredients:
    others = set(lst) - set(chosen_ones)
    counter += len(others)

print('Result for part 1: ', counter)  # 2170


### Part 2

lst_found = []
while len(lst_found) < len(d_allergens):
    for key in d_allergens:
        if len(d_allergens[key]) == 1:
            if list(d_allergens[key])[0] not in lst_found:
                lst_found.append(list(d_allergens[key])[0])
        else:
            res = d_allergens[key] - set(lst_found)
            d1 = {key: res}
            d_allergens.update(d1)

res2 = ','.join([list(d_allergens[i])[0] for i in sorted(d_allergens)])

print('Result for part 2: ', res2)  # 'nfnfk,nbgklf,clvr,fttbhdr,qjxxpr,hdsm,sjhds,xchzh'

