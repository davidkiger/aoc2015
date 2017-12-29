file = open("1-1.in", "r")

for line in file:
    moves = list(line.strip())

floor = 0
for x, i in enumerate(moves):
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1

    if floor == -1:
        print('{}'.format(x+1))
        break

print(floor)
