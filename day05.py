# --- Day 5: Supply Stacks ---
import re
from collections import deque

def parse_stacks(lines):
    stacks = None
    for l in lines:
        if l.strip() == '':
            break
        else:
            line = l.replace('    ', '[ ]')
            results = [x[1].strip() for x in re.findall(r"\[.\]", line)]

            if not stacks:
                stacks = [deque() for _ in range(len(results))]

            if results != []:
                for i in range(len(results)):
                    item = results[i]
                    if item:
                        stacks[i].appendleft(item)
    return stacks

def parse_moves(lines):
    movements = []
    for line in lines:
        if (line.startswith('move')):
            l = line.split()
            moves = (int(l[1]), int(l[3])-1, int(l[5])-1)
            movements.append(moves)
    return movements

# Part one
with open('day05_input.txt') as f:
    lines = f.readlines()
    stacks = parse_stacks(lines)
    movements = parse_moves(lines)

for move in movements:
    amount, start, end = move
    for i in range(amount):
        item = stacks[start].pop()
        stacks[end].append(item)

result_one = ""
for stack in stacks:
    result_one += stack[-1]
print(f"Part one answer - Crates on top: {result_one}")


# Part two
with open('day05_input.txt') as f:
    lines = f.readlines()
    stacks_two = parse_stacks(lines)
    movements_two = parse_moves(lines)

for move in movements_two:
    amount, start, end = move
    to_extend = deque()
    for i in range(amount):
        to_extend.appendleft(stacks_two[start].pop()) 
    stacks_two[end].extend(to_extend)


result_two = ""
for stack in stacks_two:
    result_two += stack[-1]
print(f"Part two answer - Crates on top: {result_two}")