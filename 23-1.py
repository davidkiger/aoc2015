file = open("23-1.in", "r")

instructions = []
for line in file:
    inst, args = line.strip().split(' ', 1)
    args = args.split(', ')
    if len(args) == 2:
        args[1] = int(args[1])
    if len(args) == 1 and (args[0][0] == '+' or args[0][0] == '-'):
        args[0] = int(args[0])

    instructions.append([inst, args])

i_ptr = 0
a = 0
b = 0

while True:
    # print('{} | {}'.format(a, b))
    try:
        (inst, args) = instructions[i_ptr]
    except IndexError:
        print(b)
        exit()

    if inst == 'hlf':
        if args[0] == 'a':
            a = a / 2
        elif args[0] == 'b':
            b = b / 2
        i_ptr += 1
    elif inst == 'tpl':
        if args[0] == 'a':
            a = a * 3
        elif args[0] == 'b':
            b = b * 3
        i_ptr += 1
    elif inst == 'inc':
        if args[0] == 'a':
            a = a + 1
        elif args[0] == 'b':
            b = b + 1
        i_ptr += 1
    elif inst == 'jmp':
        i_ptr += args[0]
    elif inst == 'jie':
        if args[0] == 'a' and a % 2 == 0:
            i_ptr += args[1]
        elif args[0] == 'b' and b % 2 == 0:
            i_ptr += args[1]
        else:
            i_ptr += 1
    elif inst == 'jio':
        if args[0] == 'a' and a == 1:
            i_ptr += args[1]
        elif args[0] == 'b' and b == 1:
            i_ptr += args[1]
        else:
            i_ptr += 1
