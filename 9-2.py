import itertools

file = open("9-1.in", "r")

distances = {}

for line in file:
    places, dist = line.strip().split(" = ")
    p1, p2 = places.split(" to ")

    if p1 not in distances:
        distances[p1] = {}
    if p2 not in distances:
        distances[p2] = {}

    distances[p1][p2] = int(dist)
    distances[p2][p1] = int(dist)

max_dist = 0
for path in itertools.permutations(distances.keys(), len(distances.keys())):
    dist = 0
    for i in range(len(path)-1):
        dist += distances[path[i]][path[i+1]]
    if dist > max_dist:
        max_dist = dist

print(max_dist)
