from functools import reduce


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

goal = 34000000
presents = 0
house = 0
while presents < goal:
    house += 1
    presents = sum([i*10 for i in factors(house)])

print(house)
