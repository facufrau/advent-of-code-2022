# --- Day 3: Rucksack Reorganization ---

with open('day03_input.txt') as f:
    rucksacks = f.read().strip().split('\n')

def get_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

# Part one
total_priority = 0
for items in rucksacks:
    split_index = int(len(items)/ 2) 
    first_comp = set(items[:split_index])
    second_comp = set(items[split_index:])
    common_item = (first_comp & second_comp).pop()
    total_priority += get_priority(common_item)

print(f"Part one answer - Total priority: {total_priority}")

# Part two
total_priority = 0
for i in range(0, len(rucksacks), 3):
    elf_1, elf_2, elf_3 = set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])
    badge = (elf_1 & elf_2 & elf_3).pop()
    total_priority += get_priority(badge)

print(f"Part two answer - Total priority: {total_priority}")
