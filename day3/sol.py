with open('input.txt') as f:
    l = list(map(lambda x: x.strip(), f.readlines()))

# Part 1
row_ind = 0
col_ind = 0
n = 0

while row_ind < len(l):
    char = l[row_ind][col_ind]
    if char == '#':
        n += 1
    row_ind += 1
    col_ind += 3
    col_ind = col_ind % len(l[0])

print(n)

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ans = 1

for slope in slopes:
    row_ind = 0
    col_ind = 0
    n = 0

    while row_ind < len(l):
        char = l[row_ind][col_ind]
        if char == '#':
            n += 1
        row_ind += slope[1]
        col_ind += slope[0]
        col_ind = col_ind % len(l[0])
    ans *= n

print(ans)