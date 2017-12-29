import re

vowels = re.compile(r'.*[aeiou].*[aeiou].*[aeiou].*')
double = re.compile(r'(.)\1')
bad = re.compile(r'ab|cd|pq|xy')

file = open("5-1.in", "r")

nice = 0
for line in file:
    l = line.strip()
    if vowels.search(l) and double.search(l) and not bad.search(l):
        nice += 1

print(nice)
