file = open("14-1.in", "r")

reindeer = {}
for line in file:
    tokens = line.strip().split()
    reindeer[tokens[0]] = {'speed': int(tokens[3]), 'duration': int(tokens[6]), 'rest': int(tokens[13]), 'state': 'flying', 'counter': 0, 'distance': 0, 'points': 0}

time = 2503
# time = 1000

for i in range(time):
    for deer in reindeer:
        stats = reindeer[deer]
        if stats['state'] == 'flying':
            stats['distance'] += stats['speed']
            stats['counter'] += 1
            if stats['counter'] == stats['duration']:
                stats['state'] = 'resting'
                stats['counter'] = 0
        else:
            stats['counter'] += 1
            if stats['counter'] == stats['rest']:
                stats['state'] = 'flying'
                stats['counter'] = 0

    furthest = 0
    for deer in reindeer:
        if reindeer[deer]['distance'] >= furthest:
            furthest = reindeer[deer]['distance']

    for deer in reindeer:
        if reindeer[deer]['distance'] == furthest:
            reindeer[deer]['points'] += 1

for deer in reindeer:
    print(deer, reindeer[deer]['points'])
