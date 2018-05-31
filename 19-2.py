file = open("19-1.in", "r")
# file = open("19-1.in.sample", "r")

conversions = []
for line in file:
    try:
        in_, out_ = list(line.strip().split(' => '))
        conversions.append((in_, out_))
    except ValueError:
        if len(line.strip()) > 0:
            goal = line.strip()

# This works, but it really doesn't seem like it will in all cases...
count = 0
string = goal
while string != 'e':
    for in_, out_ in conversions:
        if out_ in string:
            string = string.replace(out_, in_, 1)
            count += 1

print(count)
