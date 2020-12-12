import re

with open('input.txt') as f:
    lines = f.readlines()

bag_pattern = re.compile(r'([a-z\s]+) bags contain ')
bag_container_pattern = re.compile(r'(\d) ([a-z\s]+) bags?(?:,\s|\.)')

d_bags = dict()
for ln in lines:
    bag = re.findall(bag_pattern, ln)[0]
    bag_container = re.findall(bag_container_pattern, ln)
    if not bag_container:
        d_bags[bag] = None
    else:
        d_bags[bag] = dict((tup[1], int(tup[0])) for tup in bag_container)

# Part 1
n_bags = 0

def check_bag(bag):
    if type(bag) == dict:
        if 'shiny gold' in bag:
            print(f'shiny gold found')
            return 1
        else:
            for key in bag.keys():
                if check_bag(d_bags[key]) == 1:
                    return 1
    return 0
        

for k,v in d_bags.items():
    n_bags += check_bag(v)

print(n_bags)

# Part 2
n_bags = 0

def get_bags(bag):
    n_bags = 0
    if type(bag) == dict:
        for k,v in bag.items():
            n_bags += v
            n_bags += v * get_bags(d_bags[k])
        return n_bags
    else:
        return 0

print(get_bags(d_bags['shiny gold']))

