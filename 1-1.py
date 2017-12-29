file = open("1-1.in", "r")

for line in file:
    moves = list(line.strip())

floor = 0
for i in moves:
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1

print(floor)
