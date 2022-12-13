import re
from collections import deque

class Monkey:
    def __init__(self, A, i):
        self.read_from_input(A, i)
        self.cnt_items = 0

    def read_from_input(self, A, i):
        matchObj = re.match(r'Monkey (\d+):', A[i])
        self.id = int(matchObj.group(1))
        matchObj = re.match(r'  Starting items: ((\d|\,|\s)+)', A[i + 1])
        self.items = deque([int(n) for n in matchObj.group(1).split(", ")])
        matchObj = re.match(r'  Operation: new = (.+)', A[i + 2])
        self.term = matchObj.group(1)
        matchObj = re.match(r'  Test: divisible by (\d+)', A[i + 3])
        self.div_criteria = int(matchObj.group(1))
        matchObj = re.match(r'    If true: throw to monkey (\d+)', A[i + 4])
        self.if_true = int(matchObj.group(1))
        matchObj = re.match(r'    If false: throw to monkey (\d+)', A[i + 5])
        self.if_false = int(matchObj.group(1))

    def inspect_item_part1(self):
        old = self.items.popleft()
        new = eval(self.term)
        new //= 3
        catcher = self.if_true if new % self.div_criteria == 0 else self.if_false
        monkeys[catcher].items.append(new)
        self.cnt_items += 1

    def inspect_item_part2(self):
        old = self.items.popleft()
        new = eval(self.term) % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
        catcher = self.if_true if new % self.div_criteria == 0 else self.if_false
        monkeys[catcher].items.append(new)
        self.cnt_items += 1

    def inspect_all(self, part):
        while self.items:
            if part == 1:
                self.inspect_item_part1()
            else:
                self.inspect_item_part2()

def read_monkeys(A):
    monkeys = []
    for i in range(0, len(A), 7):
        monkeys.append(Monkey(A, i))
    return monkeys

def day11(infile):
    # reading input
    with open(infile, "r") as file:
        A = file.read().splitlines()
    global monkeys

    # solving Part One
    monkeys = read_monkeys(A)
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_all(part=1)
    B = sorted([monkey.cnt_items for monkey in monkeys])
    print("Part One: ", B[-1] * B[-2])

    # solving Part Two
    monkeys = read_monkeys(A)
    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspect_all(part=2)
    B = sorted([monkey.cnt_items for monkey in monkeys])
    print("Part Two: ", B[-1] * B[-2])