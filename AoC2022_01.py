def day01(infile):
    elves = []
    elf_cal = 0
    with open(infile, "r") as file:
        for line in file.read().splitlines():
            if line == '':
                elves.append(elf_cal)
                elf_cal = 0
            else:
                elf_cal += int(line)
    elves.append(elf_cal)
    elves.sort()

    # solving Part One
    print("Part One: ", elves[-1])

    # solving Part Two
    print("Part Two: ", elves[-1] + elves[-2] + elves[-3])