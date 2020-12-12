with open('input.txt') as f:
    lines = map(lambda x: x.strip(), f.readlines())

answers = []

curr_answer = ''
for l in lines:
    if l:
        curr_answer = ' '.join([curr_answer, l]).lstrip()
    else:
        answers.append(curr_answer)
        curr_answer = ''
answers.append(curr_answer)

# Part 1
total = 0
for answer in answers:
    total += len(set([char for char in answer if char.isalpha()]))

print(total)

# Part 2
total = 0
for answer in answers:
    n = len(answer.split(' '))
    d_counts = dict()
    for char in answer:
        if char.isalpha():
            d_counts[char] = d_counts.get(char, 0) + 1
    total += sum(1 for v in d_counts.values() if v == n)

print(total)