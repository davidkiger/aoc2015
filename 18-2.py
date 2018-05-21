file = open("18-1.in", "r")
steps = 100
# file = open("18-1.in.sample", "r")
# steps = 5


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

grid[0][0] = '#'
grid[0][size-1] = '#'
grid[size-1][0] = '#'
grid[size-1][size-1] = '#'

for step in range(steps):
    new_grid = [['.' for x in range(size)] for y in range(size)]

    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0:
                new_grid[i][j] = '#'
            elif i == 0 and j == size-1:
                new_grid[i][j] = '#'
            elif i == size-1 and j == 0:
                new_grid[i][j] = '#'
            elif i == size-1 and j == size-1:
                new_grid[i][j] = '#'
            else:
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
    '''
    for i in range(size):
        string = ''
        for j in range(size):
            string += new_grid[i][j]
        print(string)
    print('---')
    '''
    grid = new_grid

count = 0
for i in range(size):
    for j in range(size):
        if grid[i][j] == '#':
            count += 1

print(count)
