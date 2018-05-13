import itertools

file = open("17-1.in", "r")

eggnogg = 150
containers = []

for line in file:
    val = line.strip()
    containers.append(int(val))

count = 0
for i in range(len(containers)):
    for combo in itertools.combinations(containers, i):
        if sum(combo) == 150:
            count += 1

print(count)
