row = 2978
col = 3083
start = 20151125


def find_pos(r, c):
    col = 0
    pos = 0
    while col < c:
        col += 1
        pos += col

    diff = col
    row = 1
    while row < r:
        pos += diff
        diff += 1
        row += 1

    return pos


def next_code(i):
    return (i*252533) % 33554393

p = find_pos(row, col)
print(p)

num = start
for xx in range(p-1):
    num = next_code(num)

print(num)
