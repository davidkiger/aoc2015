import re

straight = re.compile(r'abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz')
doubles = re.compile(r'.*(.)\1.*(.)\2.*')

chars = list('abcdefghjkmnpqrstuvwxyz')
password = 'hxbxwxba'


def increment_password(password):
    pw_chars = list(password)
    for i in range(-1, -9, -1):
        pw_chars[i] = chars[(chars.index(pw_chars[i]) + 1) % len(chars)]
        if pw_chars[i] != 'a':
            break
    return ''.join(pw_chars)


def is_valid(p):
    return straight.search(p) and doubles.search(p)

password = increment_password(password)
while not is_valid(password):
    password = increment_password(password)

print(password)
