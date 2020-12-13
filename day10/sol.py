with open('input.txt') as f:
    l = list(map(int, f.readlines()))

device_joltage = max(l) + 3
avail_adapters = sorted(l)
joltages = [0] + avail_adapters + [device_joltage]

# Part 1
joltage_diffs = [joltages[i+1]-joltages[i] for i in range(len(joltages)-1)]

d_diffs = dict()
for jd in joltage_diffs:
    d_diffs[jd] = d_diffs.get(jd, 0) + 1

print(d_diffs[1]*d_diffs[3])

# Part 2
n = 0
d_options = dict()

for i, jd in enumerate(joltage_diffs[:-1]):
    inc = 1
    curr_jd = jd

    while inc < 3 and i+inc < len(joltage_diffs):
        if curr_jd + joltage_diffs[i+inc] <= 3:
            curr_jd += joltage_diffs[i+inc]
            inc += 1
        else:
            break
    d_options[i] = inc

d_ways = dict()

def get_options(key):
    if key not in d_options:
        return 1

    ind_range = d_options[key]
    curr_total = 0
    for tmp_key in range(key+ind_range, key, -1):
        if tmp_key not in d_ways:
            d_ways[tmp_key] = get_options(tmp_key)
        curr_total += d_ways[tmp_key]
    return curr_total



for k in sorted(d_options.keys())[::-1]:
    d_ways[k] = get_options(k)

print(get_options(0))