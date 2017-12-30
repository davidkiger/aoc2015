file = open("8-1.in", "r")

encoded = 0
code = 0

for line in file:
    chars = list(line.strip())

    encoded += 2
    for i in range(len(chars)):
        code += 1
        encoded += 1
        if chars[i] == '\\' or chars[i] == '"':
            encoded += 1

print('{}'.format(encoded-code))
