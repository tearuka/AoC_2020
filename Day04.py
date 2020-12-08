#!/usr/bin/env python
# coding: utf-8


# read input
inp = open("inp/input_04.txt").read().split("\n\n")
inp = [line.replace('\n',' ') for line in inp]


### Part 1

required_fields = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']


def contains_all(string, fields):
    for element in fields:
        if element not in string:
            return 0
    return 1


counter = 0
for line in inp:
    counter += contains_all(line,required_fields)
    
print("Result for part 1: ", counter)


### Part 2

# select only the lines that contain all fields, and split them with space separator
passports = [line.split(' ') for line in inp if contains_all(line,required_fields) == 1]

# define validity conditions
byr_min, byr_max = 1920, 2002
iyr_min, iyr_max = 2010, 2020
eyr_min, eyr_max = 2020, 2030
hgt_min_cm, hgt_max_cm = 150, 193
hgt_min_in, hgt_max_in = 59, 76
ecl_set = ['amb','blu','brn','gry','grn','hzl','oth']
import re
hcl_condition = re.compile(r'[^a-f0-9#]') # hcl -> a # followed by exactly six characters 0-9 or a-f
pid_condition = re.compile(r'[^0-9]') # pid -> a nine-digit number, including leading zeroes

# define functions for checking the charcater & number conditions
def hcl_match(strg, search=hcl_condition.search):
    return not bool(search(strg))
def pid_match(strg, search=pid_condition.search):
    return not bool(search(strg))

# function for extracting the field contents
def extract_string(substring):
    sol = [s for s in line if substring in s]
    res = sol[0].replace(substring,'')
    return(res)

# function for checking the validity of passports
def check_validity(byr,iyr,eyr,hgt,hcl,ecl,pid):
    counter = 0
    # check byr
    counter += byr_min <= int(byr) <= byr_max
    # check iyr
    counter += iyr_min <= int(iyr) <= iyr_max
    # check eyr
    counter += eyr_min <= int(eyr) <= eyr_max
    # check hgt
    if 'cm' in hgt:
        hgt = hgt.replace('cm','')
        counter += hgt_min_cm <= int(hgt) <= hgt_max_cm
    elif 'in' in hgt:
        hgt = hgt.replace('in','')
        counter += hgt_min_in <= int(hgt) <= hgt_max_in
    # check hcl
    counter += hcl[0] == '#' and len(hcl) == 7 and hcl_match(hcl) == True
    # check ecl
    counter += ecl in ecl_set
    # check pid
    counter += len(pid) == 9 and pid_match(pid) == True
    if counter == 7:
        return(1)
    else:
        return(0)

result_count = 0
for line in passports:
    # extract field contents
    byr, iyr, eyr, hgt, hcl, ecl, pid = map(extract_string,required_fields)
    # check if each passport is OK
    result_count += check_validity(byr,iyr,eyr,hgt,hcl,ecl,pid)
    
print("Result for part 2: ", result_count)

