file = open("3-1.in", "r")

grid = {(0, 0): 1}
x = [0, 0]
y = [0, 0]
for line in file:
    moves = list(line.strip())

idx = 0
for move in moves:
    if move == '^':   y[idx] -= 1
    elif move == 'v': y[idx] += 1
    elif move == '<': x[idx] -= 1
    elif move == '>': x[idx] += 1

    loc = (x[idx], y[idx])
    if loc not in grid:
        grid[loc] = 1
    else:
        grid[loc] += 1

    idx = int(not idx)

print(len(grid.keys()))
