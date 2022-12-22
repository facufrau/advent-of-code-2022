# --- Day 8: Treetop Tree House ---
with open('day08_input.txt') as f:
    grid = []
    for line in f.readlines():
        row = [int(x) for x in list(line.strip())]
        grid.append(row)

# Part one
def check_visibility(grid, x, y):
    sides = ("n", "s", "e", "w")
    visible_sides = []
    for side in sides:
        if side == "n":
            max_height = max([grid[i][x] for i in range(y-1, -1, -1)])
        elif side == "s":
            max_height = max([grid[i][x] for i in range(y+1, len(grid), 1)])
        elif side == "e":
            max_height = max([grid[y][i] for i in range(x-1, -1, -1)])
        elif side == "w":
            max_height = max([grid[y][i] for i in range(x+1, len(grid[0]), 1)])

        if max_height < grid[y][x]:
            visible_sides.append(side)

    return len(visible_sides) > 0

rows = len(grid)
cols = len(grid[0])
visible_trees = 0
for y in range(rows):
    for x in range(cols):
        if (x == 0 or y == 0) or (x == rows-1 or y == cols-1):
            visible_trees += 1
        else:
            if check_visibility(grid, x, y):
                visible_trees += 1
print(f"Part one answer - Visible trees: {visible_trees}")

# Part two
def get_scenic_score(grid, x, y):
    sides = ("n", "s", "e", "w")
    scenic_score = 1
    for side in sides:
        score = 0
        if side == "n":
            for i in range(y-1, -1, -1):
                score += 1
                if grid[i][x] >= grid[y][x]:
                    break

        elif side == "s":
            for i in range(y+1, len(grid), 1):
                score += 1
                if grid[i][x] >= grid[y][x]:
                    break

        elif side == "e":
            for i in range(x-1, -1, -1):
                score += 1
                if grid[y][i] >= grid[y][x]:
                    break

        elif side == "w":
            for i in range(x+1, len(grid[0]), 1):
                score += 1
                if grid[y][i] >= grid[y][x]:
                    break

        scenic_score *= score

    return scenic_score

max_score = 0
for y in range(rows):
    for x in range(cols):
        if (x > 0 and x < rows-1) and (y > 0 and y < cols-1):
            score = get_scenic_score(grid, x, y)
            if score > max_score:
                max_score = score
print(f"Part two answer - Max Scenic Score: {max_score}")