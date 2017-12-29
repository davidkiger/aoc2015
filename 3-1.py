file = open("3-1.in", "r")

grid = {(0, 0): 1}
x = 0
y = 0
for line in file:
    moves = list(line.strip())

for move in moves:
    if move == '^':   y -= 1
    elif move == 'v': y += 1
    elif move == '<': x -= 1
    elif move == '>': x += 1

    loc = (x, y)
    if loc not in grid:
        grid[loc] = 1
    else:
        grid[loc] += 1

print(len(grid.keys()))
