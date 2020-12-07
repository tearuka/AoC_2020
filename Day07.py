#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_07.txt").read().splitlines()

bags = [line.replace('bags','bag').replace('.','').split(' contain ') for line in inp]


### Part 1

def find_bags(data):
    RES = []
    lst = ['shiny gold bag']
    while lst != []:
        lst_res = []
        for bag_name in lst:
            for line in data:
                if bag_name in line[1]:
                    lst_res.append(line[0])
                    RES.append(line[0])
        lst = lst_res
    return(len(set(RES)))

res1 = find_bags(bags)

print("Result for part 1: ", res1)


### Part 2

def search_for_bag(data):
    counter = 0
    lst = ['shiny gold bag']
    lstn = [1]
    while lst != []:
        lst_name = []
        lst_num = []
        for line in data:
            i = 0
            for bag_name in lst:
                if bag_name in line[0]:
                    sublist_of_bags = line[1].split(', ')
                    for bag in sublist_of_bags:
                        num = bag[0]
                        name = bag[2:]
                        # do only if there are smaller bags still 
                        if num != 'n':
                            new_num = int(lstn[i]) * int(num)
                            lst_name.append(name)
                            lst_num.append(new_num)
                            counter += new_num
                i += 1
        lst = lst_name
        lstn = lst_num
    return(counter)

res2 = search_for_bag(bags)

print("Result for part 2: ", res2)

