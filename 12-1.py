import re

file = open("12-1.in", "r")

tokens = []
for line in file:
    tokens = re.split(',|\[|\]|\{|\}|"|:', line.strip())
    tokens = list(filter(None, tokens))

total = 0
for x in tokens:
    try:
        total += int(x)
    except ValueError:
        pass

print(total)
