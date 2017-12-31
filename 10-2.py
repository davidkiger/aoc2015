string = '1113122113'


def seesay(s):
    new_string = ''
    digits = list(s)
    digit = digits[0]
    count = 1
    for i in range(1, len(digits)):
        if digits[i] == digit:
            # Continuing
            count += 1
        else:
            # Appending and resetting
            new_string = '{}{}{}'.format(new_string, count, digit)
            digit = digits[i]
            count = 1
    new_string = '{}{}{}'.format(new_string, count, digit)

    return new_string

# print(string)
for i in range(50):
    string = seesay(string)
    # print(string)

print(len(string))
