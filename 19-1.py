file = open("19-1.in", "r")
# file = open("19-1.in.sample", "r")

conversions = {}
for line in file:
    try:
        in_, out_ = list(line.strip().split(' => '))
        try:
            conversions[in_].append(out_)
        except KeyError:
            conversions[in_] = []
            conversions[in_].append(out_)
    except ValueError:
        if len(line.strip()) > 0:
            string = line.strip()

key = ''
strings = set()
for i in range(len(string)):
    key += string[i]
    if i+1 >= len(string) or string[i+1] in list('eABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        if key in conversions.keys():
            for repl in conversions[key]:
                # print(string)
                # print('{} => {}'.format(key, repl))
                if len(key) == 1:
                    # print(string[:i])
                    # print(repl)
                    # print(string[(i+len(key)):])
                    new_string = string[:i] + repl + string[(i+len(key)):]
                    strings.add(new_string)
                else:
                    # print(string[:i-1])
                    # print(repl)
                    # print(string[(i+len(key)-1):])
                    new_string = string[:i-1] + repl + string[(i+len(key)-1):]
                    strings.add(new_string)
                # print(new_string)
                # print('-----')
        key = ''

print(len(strings))
