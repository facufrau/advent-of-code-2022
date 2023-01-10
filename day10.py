# --- Day 8: Treetop Tree House ---
with open('day10_input.txt') as f:
    lines = [line.strip().split() for line in f.readlines()]

# Part one   
register = 1
cycle = 1
check = 20
total_signal = 0

for line in lines:
    if len(line) == 1:
        cycle += 1
        if cycle == check:
            total_signal += register * cycle
            check += 40
    else:
        for i in range(2):
            if i > 0:
                register += int(line[1])
            cycle += 1
            
            if cycle == check:
                total_signal += register * cycle
                check += 40
print(f"Part one answer - Total Signal Strength: {total_signal}")


# Part two
sprite = 1
cycle = 0
row = 0
crt = ["" for _ in range(6)]

def check_position(sprite_pos, cycle_num):
    return abs(sprite_pos - cycle_num) < 2


def draw_pxl(crt_array, row_num, sprite_pos, cycle_num):
    if check_position(sprite_pos, cycle_num):
        draw = "#"
    else:
        draw = "."
    crt_array[row_num] += (draw)


for line in lines:
    if len(line) == 1:
        draw_pxl(crt, row, sprite, cycle)
        cycle += 1
        if cycle == 40:
            row += 1
            cycle = cycle % 40
    else:
        for i in range(2):
            draw_pxl(crt, row, sprite, cycle)
            if i > 0:
                sprite += int(line[1])
            cycle += 1
            if cycle == 40:
                row += 1
                cycle = cycle % 40

# Part two answer
for r in crt:
    print(r)