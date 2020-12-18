#!/usr/bin/env python
# coding: utf-8


# read input
inp = open('inp/input_18.txt').read().splitlines()
inp = [line.replace(' ','') for line in inp]


# using a stack to store values : one stack for numbers, one for operators

def perform_operation(x, y, operator):
    if operator == '+':
        return x + y
    if operator == '*':
        return x * y


def precedence(operator, prec):
    if operator == '+':
        if prec == 'sum':
            return 2
        else:
            return 1
    if operator == '*':
        if prec == 'multi':
            return 2
        else:
            return 1
    if operator in ('(',')'):
        return 0


def evaluate_expression(string, prec):
    numbers = []
    operators = []
    for char in string:
        if char.isdigit():
            numbers.append(int(char))
        elif char in ('+','*'):
            while operators and precedence(char, prec) <= precedence(operators[-1], prec):
                numbers.append(get_and_perform(numbers,operators))
            operators.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators and operators[-1] != '(':
                numbers.append(get_and_perform(numbers,operators))
            operators.pop()
    while operators:
        numbers.append(get_and_perform(numbers,operators))
    return numbers[-1]


def get_and_perform(numbers, operators):
    a = numbers.pop()
    b = numbers.pop()
    op = operators.pop()
    result = perform_operation(a, b, op)
    return result


counter = 0
for line in inp:
    counter += evaluate_expression(line, 'none')

print('Result for part 1: ', counter)  # 2743012121210


counter = 0
for line in inp:
    counter += evaluate_expression(line, 'sum')

print('Result for part 2: ', counter)  # 65658760783597
