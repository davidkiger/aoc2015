file = open("6-1.in", "r")

instructions = []
for line in file:
    tokens = line.strip().split(" ")
    if tokens[0] == 'turn':
        command = [tokens[1], tokens[2], tokens[4]]
    elif tokens[0] == 'toggle':
        command = [tokens[0], tokens[1], tokens[3]]

    instructions.append(command)

grid = [[0 for i in range(1000)] for j in range(1000)]
for inst in instructions:
    action, start, end = inst
    start_x, start_y = [int(x) for x in start.split(",")]
    end_x, end_y = [int(x) for x in end.split(",")]

    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            if action == 'on':
                grid[x][y] += 1
            elif action == 'off':
                grid[x][y] = max(0, grid[x][y] - 1)
            elif action == 'toggle':
                grid[x][y] += 2

print(sum(map(sum, grid)))
