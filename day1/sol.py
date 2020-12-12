with open('input.txt') as f:
    l = list(map(int, f.readlines()))

# Part 1
for i, num1 in enumerate(l):
    for num2 in l[i+1:]:
        if num1 + num2 == 2020:
            print(num1, num2)
            print(num1 * num2)

# Part 2
for i, num1 in enumerate(l):
    for j, num2 in enumerate(l[i+1:]):
        for num3 in l[i+j+1:]:
            if num1 + num2 + num3 == 2020:
                print(num1, num2, num3)
                print(num1 * num2 * num3)