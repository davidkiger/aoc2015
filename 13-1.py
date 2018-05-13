import itertools

file = open("13-1.in", "r")

pairs = {}
for line in file:
    tokens = line.strip().split()
    name = tokens[0]
    value = int(tokens[3])
    if tokens[2] == 'lose':
        value *= -1
    other = tokens[10][:-1]
    try:
        pairs[name][other] = value
    except KeyError:
        pairs[name] = {}
        pairs[name][other] = value

max_happiness = 0
for path in itertools.permutations(pairs.keys(), len(pairs.keys())):
    happiness = 0
    for i in range(len(path)):
        happiness += pairs[path[i]][path[(i+1) % len(path)]]
        happiness += pairs[path[i]][path[(i-1) % len(path)]]
    # print(path, happiness)
    max_happiness = max(happiness, max_happiness)

print(max_happiness)
