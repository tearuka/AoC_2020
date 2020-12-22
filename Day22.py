#!/usr/bin/env python
# coding: utf-8


# read input
inp = open('inp/input_22.txt').read()

deck1, deck2 = inp.split('\n\n')
deck1 = [int(line) for line in deck1.split('\n')[1:]]
deck2 = [int(line) for line in deck2.split('\n')[1:]]


### Part 1

def crab_combat(deck1, deck2):
    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card1 < card2:
            deck2.append(card2)
            deck2.append(card1)
        else:
            print('Both players have the same card')
    return 1 if deck1 else 2


def calculate_result(winner):
    result = 0
    lst = deck1 if winner == 1 else deck2
    for i in range(len(lst)):
        result += (len(lst) - i) * lst[i]
    return result


winner = crab_combat(deck1, deck2)
res1 = calculate_result(winner)

print('Result for part 1: ', res1)  # 35202


### Part 2

deck1, deck2 = inp.split('\n\n')
deck1 = [int(line) for line in deck1.split('\n')[1:]]
deck2 = [int(line) for line in deck2.split('\n')[1:]]

def beat_the_crab(deck1, deck2):
    visited1 = []
    visited2 = []
    while deck1 and deck2:
        if deck1 in visited1 or deck2 in visited2:
            return 1
        visited1.append(deck1.copy())
        visited2.append(deck2.copy())
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if len(deck1) >= card1 and len(deck2) >= card2:
            deck1_ingame = deck1[:card1].copy()
            deck2_ingame = deck2[:card2].copy()
            winner = beat_the_crab(deck1_ingame, deck2_ingame)
        else:
            if card1 > card2:
                winner = 1
            elif card1 < card2:
                winner = 2
        if winner == 1:
            deck1.append(card1)
            deck1.append(card2)
        elif winner == 2:
            deck2.append(card2)
            deck2.append(card1)
    return 1 if deck1 else 2


winner = beat_the_crab(deck1, deck2)
res2 = calculate_result(winner)

print('Result for part 2: ', res2)  # 32317
