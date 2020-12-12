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
