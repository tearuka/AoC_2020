#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_12.txt").read().splitlines()
instructions = [line[0] for line in inp]
values = [int(line[1:]) for line in inp]


### Part 1

def navigate(data):
    x, y = 0, 0  # ship coordinates
    facing = 90  # ship facing east
    for i in range(len(instructions)):
        if instructions[i] == 'N':
            y += values[i]
        elif instructions[i] == 'S':
            y -= values[i]
        elif instructions[i] == 'E':
            x += values[i]
        elif instructions[i] == 'W':
            x -= values[i]
        elif instructions[i] == 'R':
            facing += values[i]
            if facing >= 360:
                facing -= 360
            elif facing < 0:
                facing += 360
        elif instructions[i] == 'L':
            facing -= values[i]
            if facing >= 360:
                facing -= 360
            elif facing < 0:
                facing += 360
        elif instructions[i] == 'F':
            if facing == 0:
                y += values[i]
            elif facing == 180:
                y -= values[i]
            elif facing == 90:
                x += values[i]
            if facing == 270:
                x -= values[i]
    return abs(x) + abs(y)

res1 = navigate(inp)
print('Result for part 1: ', res1)  # 562


### Part 2

def navigate_with_waypoint(data):
    x, y = 0, 0  # ship coordinates
    wx, wy = 10, 1 # waypoint coordinates relative to the ship
    for i in range(len(instructions)):
        if instructions[i] == 'N':
            wy += values[i]
        elif instructions[i] == 'S':
            wy -= values[i]
        elif instructions[i] == 'E':
            wx += values[i]
        elif instructions[i] == 'W':
            wx -= values[i]
        elif instructions[i] == 'R':
            if values[i] == 90:
                wx, wy = wy, -wx
            elif values[i] == 180:
                wx, wy = -wx, -wy
            elif values[i] == 270:
                wx, wy = -wy, wx
        elif instructions[i] == 'L':
            if values[i] == 90:
                wx, wy = -wy, wx
            elif values[i] == 180:
                wx, wy = -wx, -wy
            elif values[i] == 270:
                wx, wy = wy, -wx
        elif instructions[i] == 'F':
            x += values[i] * wx
            y += values[i] * wy               
    return abs(x) + abs(y)

res2 = navigate_with_waypoint(inp)
print('Result for part 2: ', res2)  # 101860
