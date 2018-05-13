file = open("16-1.in", "r")

features = {'children': -1, 'cats': -1, 'samoyeds': -1, 'pomeranians': -1, 'akitas': -1, 'vizslas': -1, 'goldfish': -1, 'trees': -1, 'cars': -1, 'perfumes': -1}
# sues = {}
matched_sue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for line in file:
    sue, objects = line.strip().split(': ', 1)
    _, number = sue.split(' ')
    number = int(number)
    these_features = features.copy()
    objects = objects.split(', ')
    for o in objects:
        obj, count = o.split(': ')
        these_features[obj] = int(count)

    found = True
    for key in features.keys():
        if not (these_features[key] == matched_sue[key] or these_features[key] == -1):
            found = False

    if found:
        print(number)
