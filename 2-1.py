file = open("2-1.in", "r")

packages = []
for line in file:
    packages.append([int(x) for x in line.strip().split("x")])

total = 0
for p in packages:
    l, w, h = p
    total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

print(total)
