with open('input.txt') as f:
    lns = list(map(lambda x: x.strip(), f.readlines()))

# Part 1
seat_ids = []

for l in lns:
    n_rows = 128
    n_cols = 8
    row_bounds = [0, 127]
    col_bounds = [0,7]

    for char in l[:7]:
        n_rows /= 2
        if char == 'F':
            row_bounds[1] -= n_rows
        else: # then char == 'B'
            row_bounds[0] += n_rows
    if row_bounds[0] != row_bounds[1]:
        print(row_bounds)
    row = row_bounds[0]

    for char in l[7:]:
        n_cols /= 2
        if char == 'L':
            col_bounds[1] -= n_cols
        else:
            col_bounds[0] += n_cols
    if col_bounds[0] != col_bounds[1]:
        print(col_bounds)
    col = col_bounds[0]

    seat_id = 8 * row + col
    seat_ids.append(seat_id)

print(max(seat_ids))

# Part 2
s = set(seat_ids)

for row_ind in range(1, 127):
    for col_ind in range(8):
        tmp_seat_id = 8 * row_ind + col_ind
        neighbors = set([tmp_seat_id-1, tmp_seat_id+1])
        if tmp_seat_id not in s and len(neighbors.difference(s)) == 0:
            print(tmp_seat_id)