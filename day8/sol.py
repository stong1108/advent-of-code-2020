with open('input.txt') as f:
    lns = map(lambda x: x.strip(), f.readlines())

instructions = dict(enumerate(lns))

# Part 1
completed = set()
curr_ind = 0
accumulator = 0

while curr_ind not in completed:
    completed.add(curr_ind)

    string = instructions[curr_ind]
    cmd, val = string.split(' ')
    val = int(val)

    if cmd == 'jmp':
        curr_ind += val
    elif cmd == 'acc':
        accumulator += val
        curr_ind += 1
    elif cmd == 'nop':
        curr_ind += 1

print(accumulator)

# Part 2
for ind in sorted(instructions.keys()):
    if instructions[ind].startswith('acc'):
        continue
    
    else:
        orig = instructions[ind]
        switched = instructions[ind].replace('nop', 'jmp')
        if switched == instructions[ind]:
            switched = instructions[ind].replace('jmp', 'nop')
        instructions[ind] = switched
        
    completed = set()
    curr_ind = 0
    accumulator = 0

    while curr_ind not in completed:
        if curr_ind == max(instructions.keys()):
            print(accumulator)
            break
        completed.add(curr_ind)

        string = instructions[curr_ind]
        cmd, val = string.split(' ')
        val = int(val)

        if cmd == 'jmp':
            curr_ind += val
        elif cmd == 'acc':
            accumulator += val
            curr_ind += 1
        elif cmd == 'nop':
            curr_ind += 1
    
    instructions[ind] = orig


