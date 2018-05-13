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

    found = (
        (these_features['children'] == matched_sue['children'] or these_features['children'] == -1) and
        (these_features['cats'] > matched_sue['cats'] or these_features['cats'] == -1) and
        (these_features['samoyeds'] == matched_sue['samoyeds'] or these_features['samoyeds'] == -1) and
        (these_features['pomeranians'] < matched_sue['pomeranians'] or these_features['pomeranians'] == -1) and
        (these_features['akitas'] == matched_sue['akitas'] or these_features['akitas'] == -1) and
        (these_features['vizslas'] == matched_sue['vizslas'] or these_features['vizslas'] == -1) and
        (these_features['goldfish'] < matched_sue['goldfish'] or these_features['goldfish'] == -1) and
        (these_features['trees'] > matched_sue['trees'] or these_features['trees'] == -1) and
        (these_features['cars'] == matched_sue['cars'] or these_features['cars'] == -1) and
        (these_features['perfumes'] == matched_sue['perfumes'] or these_features['perfumes'] == -1)
    )

    if found:
        print(number)
