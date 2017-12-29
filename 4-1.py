import hashlib
m = hashlib.md5()

key = 'bgvyzdsv'
i = 0

while True:
    md5 = hashlib.md5("{}{}".format(key, i).encode('utf8')).hexdigest()
    if md5.startswith('00000'):
        print(i)
        break
    i += 1
