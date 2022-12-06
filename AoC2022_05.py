def init_stacks(lines, line_num, stack_num):
    stacks = [[] for i in range(stack_num)]
    for line in lines[:line_num]:
        for i, c in enumerate(list(line)[1::4]):
            if c != ' ':
                stacks[i].append(c)
    for S in stacks:
        S.reverse()
    return stacks

def perform_move(stacks, line, reverse):
    words = line.split(' ')
    quantity = int(words[1])
    from_where = int(words[3]) - 1
    to_where = int(words[5]) - 1

    stacks[to_where].extend(reversed(stacks[from_where][-quantity:])
                            if reverse
                            else stacks[from_where][-quantity:])
    del stacks[from_where][-quantity:]

def solve(lines, line_num, stack_num, reverse):
    stacks = init_stacks(lines, line_num, stack_num)
    for line in lines[line_num + 2:]:
        perform_move(stacks, line, reverse)
    for S in stacks:
        print(S[-1], end="")
    print()

def day05(infile):
    with open(infile, "r") as file:
        lines = file.read().splitlines()

    for line_num, line in enumerate(lines):
        if line.startswith(" 1"):
            stack_num = (len(line) + 2) // 4
            break

    # solving Part One
    print("Part One:", end=" ")
    solve(lines, line_num, stack_num, reverse=True)

    # solving Part Two
    print("Part Two:", end=" ")
    solve(lines, line_num, stack_num, reverse=False)