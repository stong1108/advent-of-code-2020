with open('input.txt') as f:
    lns = map(lambda x: x.strip(), f.readlines())

curr_pos = (0, 0, 0) # i, j, theta

angles = {0: 'E',
        360: 'E',
        90: 'N',
        -270: 'N',
        180: 'W', 
        -180: 'W',
        270: 'S',
        -90: 'S'
        }

d_cmd = {'N': (1, 0, 0),
        'S': (-1, 0, 0),
        'E': (0, 1, 0),
        'W': (0, -1, 0),
        'L': (0, 0, 1),
        'R': (0, 0, -1)
        }
# Part 1

for ln in lns:
    cmd = ln[0]
    val = int(ln[1:])

    if cmd == 'F':
        direction = d_cmd[angles[curr_pos[2]]]
    else:
        direction = d_cmd[cmd]
    new_pos = tuple(curr_pos[i] + ind*val for i, ind in enumerate(direction))
    
    reduced_dir = new_pos[2] % 360
    curr_pos = (new_pos[0], new_pos[1], reduced_dir)

print(curr_pos)

# Part 2
wp_pos = (1, 10, 0)
curr_pos = (0, 0, 0)

for ln in lns:
    cmd = ln[0]
    val = int(ln[1:])

    if cmd == 'F':
        direction = wp_pos
        curr_pos = tuple(curr_pos[i] + ind*val for i, ind in enumerate(direction))
    else:
        direction = d_cmd[cmd]
        wp_tmp = tuple(wp_pos[i] + ind*val for i, ind in enumerate(direction))
        if wp_tmp[2] != 0:
            rotations = wp_tmp[2] / 90
            if rotations < 0:
                while rotations != 0:
                    wp_tmp = (-wp_tmp[1], wp_tmp[0], 0)
                    rotations += 1
            elif rotations > 0:
                while rotations != 0:
                    wp_tmp = (wp_tmp[1], -wp_tmp[0], 0)
                    rotations -= 1
                # right: (10, 4) -> (4, -10) -> (-10, -4) -> (-4, 10)
                # left: (10, 4) -> (-4, 10) -> (-10, -4), (4, -10)
    wp_pos = wp_tmp

print(f'wp_pos: {wp_pos}')
print(f'curr_pos: {curr_pos}')

