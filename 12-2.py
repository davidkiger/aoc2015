import json


def parse_obj(o):
    tmp_val = 0
    for k, v in o.items():
        if v == 'red':
            return 0
        try:
            tmp_val += int(v)
        except (TypeError, ValueError):
            if type(v) is list:
                tmp_val += parse_list(v)
            elif type(v) is dict:
                tmp_val += parse_obj(v)
    return tmp_val


def parse_list(l):
    tmp_val = 0
    for v in l:
        try:
            tmp_val += int(v)
        except (TypeError, ValueError):
            if type(v) is list:
                tmp_val += parse_list(v)
            elif type(v) is dict:
                tmp_val += parse_obj(v)
    return tmp_val


file = open("12-1.in", "r")

for line in file:
    obj = json.loads(line.strip())

total = parse_list(obj)
print(total)
