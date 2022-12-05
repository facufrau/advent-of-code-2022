# --- Day 4: Camp Cleanup ---

with open('day04_input.txt') as f:
    pairs = [x.split(',') for x in f.read().split('\n')]

# Part one and two
overlaps_one ,overlaps_two = 0, 0
for pair in pairs:
    pair_1 = [int(x) for x in pair[0].split('-')]
    pair_2 = [int(x) for x in pair[1].split('-')]

    if pair_1[0] >= pair_2[0] and pair_1[1] <= pair_2[1]:
        overlaps_one += 1
    elif pair_2[0] >= pair_1[0] and pair_2[1] <= pair_1[1]:
        overlaps_one += 1

    if (pair_2[0] <= pair_1[0] <= pair_2[1]) or (pair_2[0] <= pair_1[1] <= pair_2[1]):
        overlaps_two += 1
    elif (pair_1[0] <= pair_2[0] <= pair_1[1]) or (pair_1[0] <= pair_2[1] <= pair_1[1]):
        overlaps_two += 1

print(f"Part one answer - Total overlaps: {overlaps_one}")
print(f"Part two answer - Total overlaps: {overlaps_two}")