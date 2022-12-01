# --- Day 1: Calorie Counting ---

# Part one and two
with open('day01_input.txt') as f:
    elves_cals = [int(x) if x != '\n' else 'x' for x in f.readlines() ]
    max_calories = 0
    calories = 0
    total_calories = []
    for item in elves_cals:
        if (item == 'x'):
            if calories > max_calories:
                max_calories = calories
            total_calories.append(calories)
            calories = 0
        else:
            calories += item

total_calories.sort(reverse=True)

print(f"Part one answer - Max calories: {max_calories}")
print(f"Part two answer - Top 3 calories: {sum(total_calories[:3])}")
