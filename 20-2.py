import numpy as np

goal = 34000000
presents = np.zeros(1000000)

for elf in range(1, 1000000):
    presents[elf:(elf+1)*50:elf] += 11*elf

    if len(np.nonzero(presents >= goal)[0]) > 0:
        print(np.nonzero(presents >= goal)[0])
        exit()
