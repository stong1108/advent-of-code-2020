with open('input.txt') as f:
    lns = list(map(lambda x: x.strip(), f.readlines()))

i_bounds = range(len(lns))
j_bounds = range(len(lns[0]))

# Part 1
def get_adj_inds(i, j):
    adj = [(i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1), (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)]
    adj_inds = [tup for tup in adj if tup[0] in i_bounds and tup[1] in j_bounds]
    return adj_inds

changes = 1
while changes != 0:
    changes = 0
    new_lns = []
    for i_ind, ln in enumerate(lns):
        new_ln = ''
        for j_ind, char in enumerate(ln):
            adj_inds = get_adj_inds(i_ind, j_ind)
            adj_chars = [lns[tup[0]][tup[1]] for tup in adj_inds]
            n_occupied = sum(1 for ac in adj_chars if ac == '#')

            if char == 'L' and n_occupied == 0:
                new_ln += '#'
                changes += 1
            elif char == '#' and n_occupied >= 4:
                new_ln += 'L'
                changes += 1
            else:
                new_ln += char
        new_lns.append(new_ln)
    lns = new_lns
    
print(sum(1 for ln in lns for char in ln if char == '#'))

# Part 2

def check_adj_dir(i, j, lns):
    n_occupied = 0
    factor = 1

    d_incr = {'upleft': (-1, -1), 'up': (-1, 0), 'upright': (-1, 1),
        'left': (0, -1), 'right': (0, 1),
        'downleft': (1, -1), 'down': (1, 0), 'downright': (1, 1)
        }
    
    while len(d_incr) > 0:
        done_dirs = set()
        for direction, inds in d_incr.items():
            ind_to_check = (i + factor*inds[0], j + factor*inds[1])
            if ind_to_check[0] not in i_bounds or ind_to_check[1] not in j_bounds:
                done_dirs.add(direction)
            else:
                char_to_check =  lns[ind_to_check[0]][ind_to_check[1]]
                if char_to_check != '.':
                    done_dirs.add(direction)
                    if char_to_check == '#':
                        n_occupied += 1

        d_incr = dict((k,v) for k,v in d_incr.items() if k not in done_dirs)
        factor += 1
    return n_occupied


changes = 1
while changes != 0:
    changes = 0
    new_lns = []
    for i_ind, ln in enumerate(lns):
        new_ln = ''
        for j_ind, char in enumerate(ln):
            if char == '.':
                new_ln += char
            else:
                n_occupied = check_adj_dir(i_ind, j_ind, lns)
                if char == 'L' and n_occupied == 0:
                    new_ln += '#'
                    changes += 1
                elif char == '#' and n_occupied >= 5:
                    new_ln += 'L'
                    changes += 1
                else:
                    new_ln += char

        new_lns.append(new_ln)
    lns = new_lns
print(sum(1 for ln in lns for char in ln if char == '#'))
