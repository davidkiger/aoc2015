file = open("2-1.in", "r")

packages = []
for line in file:
    packages.append([int(x) for x in line.strip().split("x")])

ribbon = 0
for p in packages:
    ribbon += p[0]*p[1]*p[2]
    p.remove(max(p))
    ribbon += 2*p[0] + 2*p[1]

print(ribbon)
