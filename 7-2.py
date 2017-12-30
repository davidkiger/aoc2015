import copy

file = open("7-1.in", "r")


def runthrough(instructions, wires):
    while len(instructions):
        for inst in instructions:
            if inst[0] == 'COPY':
                try:
                    wires[inst[2]] = int(inst[1])
                    instructions.remove(inst)
                except ValueError:
                    if inst[1] in wires:
                        wires[inst[2]] = wires[inst[1]]
                        instructions.remove(inst)
            elif inst[0] == 'NOT' and inst[1] in wires:
                wires[inst[2]] = (~wires[inst[1]]) & 0xFFFF
                instructions.remove(inst)
            elif inst[0] == 'AND':
                val = None
                try:
                    val = int(inst[1][0])
                except ValueError:
                    pass

                try:
                    val = wires[inst[1][0]]
                except KeyError:
                    pass

                if val is not None:
                    try:
                        wires[inst[2]] = (val & wires[inst[1][1]]) & 0xFFFF
                        instructions.remove(inst)
                    except KeyError:
                        pass
            elif inst[0] == 'OR':
                try:
                    wires[inst[2]] = (wires[inst[1][0]] | wires[inst[1][1]]) & 0xFFFF
                    instructions.remove(inst)
                except KeyError:
                    pass
            elif inst[0] == 'RSHIFT':
                try:
                    wires[inst[2]] = (wires[inst[1][0]] >> int(inst[1][1])) & 0xFFFF
                    instructions.remove(inst)
                except KeyError:
                    pass
            elif inst[0] == 'LSHIFT':
                try:
                    wires[inst[2]] = (wires[inst[1][0]] << int(inst[1][1])) & 0xFFFF
                    instructions.remove(inst)
                except KeyError:
                    pass


wires = {}
instructions = []
second_instructions = []
for line in file:
    _in, _out = line.strip().split(" -> ")
    _in = _in.split(' ')
    if len(_in) == 1:
        instructions.append(['COPY', _in[0], _out])
    elif len(_in) == 2:
        instructions.append(['NOT', _in[1], _out])
    elif len(_in) == 3:
        instructions.append([_in[1], [_in[0], _in[2]], _out])

second_instructions = copy.deepcopy(instructions)

runthrough(instructions, wires)
print(wires['a'])

tmp = wires['a']
for i in second_instructions:
    if i[2] == 'b':
        i[1] = tmp

wires = {}
runthrough(second_instructions, wires)
print(wires['a'])
