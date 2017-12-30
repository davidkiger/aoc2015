file = open("8-1.in", "r")

code = 0
memory = 0

for line in file:
    chars = list(line.strip())

    chars = chars[1:-1]
    code += 2
    skip = 0
    for i in range(len(chars)):
        code += 1
        if skip:
            skip -= 1
            continue

        if chars[i] == '\\':
            if chars[i+1] == '\\' or chars[i+1] == '"':
                skip = 1
            elif chars[i+1] == 'x':
                skip = 3

        memory += 1

print('{}'.format(code-memory))
