file = open("18-1.in", "r")
steps = 100
# file = open("18-1.in.sample", "r")
# steps = 4


def get_count_neighbors(grid, x, y):
    count = 0
    if x-1 >= 0 and y-1 >= 0 and grid[x-1][y-1] == '#':
        count += 1
    if y-1 >= 0 and grid[x][y-1] == '#':
        count += 1
    if x+1 < len(grid) and y-1 >= 0 and grid[x+1][y-1] == '#':
        count += 1
    if x-1 >= 0 and grid[x-1][y] == '#':
        count += 1
    if x+1 < len(grid) and grid[x+1][y] == '#':
        count += 1
    if x-1 >= 0 and y+1 < len(grid) and grid[x-1][y+1] == '#':
        count += 1
    if y+1 < len(grid) and grid[x][y+1] == '#':
        count += 1
    if x+1 < len(grid) and y+1 < len(grid) and grid[x+1][y+1] == '#':
        count += 1
    return count

grid = []
for line in file:
    nodes = list(line.strip())
    grid.append(nodes)

size = len(grid)
for step in range(steps):
    new_grid = [['.' for x in range(size)] for y in range(size)]

    for i in range(size):
        for j in range(size):
            neighbors = get_count_neighbors(grid, i, j)
            if grid[i][j] == '#':
                if neighbors == 2 or neighbors == 3:
                    new_grid[i][j] = '#'
                else:
                    new_grid[i][j] = '.'
            else:
                if neighbors == 3:
                    new_grid[i][j] = '#'
                else:
                    new_grid[i][j] = '.'

    grid = new_grid

count = 0
for i in range(size):
    for j in range(size):
        if grid[i][j] == '#':
            count += 1

print(count)
