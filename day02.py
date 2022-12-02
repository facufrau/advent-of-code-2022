# --- Day 2: Rock Paper Scissors ---

with open('day02_input.txt') as f:
    rounds = [x.split() for x in f.read().split('\n')]

player_wins = [['C', 'X'], ['A', 'Y'], ['B', 'Z']]
draw = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
player_loses = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]
points_one = {'X': 1, 'Y': 2, 'Z': 3}

# Part one
score = 0
for round in rounds:
    move_points = points_one[round[1]]
    if round in player_wins:
        score += move_points + 6
    elif round in draw:
        score += move_points + 3
    else:
        score += move_points
print(f"Part one answer - Player score: {score}")

# Part two
points_two = {'AX': 3, 'BX': 1, 'CX': 2,
              'AY': 4, 'BY': 5, 'CY': 6,
              'AZ': 8, 'BZ': 9, 'CZ': 7}
score = 0
for round in rounds:
    score += points_two[''.join(round)]
print(f"Part two answer - Player score: {score}")