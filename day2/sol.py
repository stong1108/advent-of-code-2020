import re

with open('input.txt') as f:
    l = f.readlines()

# Part 1
n_valid_passwords = 0
pattern = re.compile(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
for line in l:
    match_list = re.findall(pattern, line)

    try:
        tup = match_list[0]
        n_min = int(tup[0])
        n_max = int(tup[1])
        n = sum([1 for char in tup[3] if char == tup[2]])
        if n >= n_min and n <= n_max:
            n_valid_passwords += 1
    except IndexError:
        print(f'error: {line}')

print(n_valid_passwords)

# Part 2
n_valid_passwords = 0
pattern = re.compile(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
for line in l:
    match_list = re.findall(pattern, line)

    try:
        tup = match_list[0]
        ind1 = int(tup[0]) - 1 
        ind2 = int(tup[1]) - 1
        if int(tup[3][ind1] == tup[2]) + int(tup[3][ind2] == tup[2]) == 1:
            n_valid_passwords += 1
    except IndexError:
        print(f'error: {line}')

print(n_valid_passwords)