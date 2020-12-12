import itertools

with open('input.txt') as f:
    l = list(map(int, f.readlines()))

# Part 1
curr_ind = 25
for min_ind in range(len(l)-25):
    target = l[curr_ind]

    pairs = itertools.combinations(l[min_ind:curr_ind], 2)
    pair_sums = set(sum(tup) for tup in pairs)

    if target in pair_sums:
        curr_ind += 1
    else:
        print(f"can't sum to {target}: {l[min_ind:curr_ind]}")
        break

# Part 2
target = 20874512
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        window = l[i:j]
        if sum(window) == target:
            print(i, j)
            print(f'{min(window)}, {max(window)}')
            print(f'{min(window)+max(window)}')