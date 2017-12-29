import re

repeats = re.compile(r'(..).*\1')
skip = re.compile(r'(.).\1')

file = open("5-1.in", "r")

nice = 0
for line in file:
    l = line.strip()
    if repeats.search(l) and skip.search(l):
        nice += 1

print(nice)
