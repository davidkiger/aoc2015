'''
Sugar:     capacity 3,  durability 0, flavor 0,  texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0,  texture 0,  calories 9
Candy:     capacity -1, durability 0, flavor 4,  texture 0,  calories 1
Chocolate: capacity 0,  durability 0, flavor -2, texture 2,  calories 8

c = sugar*3 - sprinkles*3 - candy
d = sprinkles*3
f = candy*4 - chocolate*2
t = chocolate*2 - sugar*3
'''
high = 0
recipe = None
for iCandy in range(1, 101):
    counts = {'Candy': iCandy}
    for iSprinkles in range(1, 101-iCandy):
        counts['Sprinkles'] = iSprinkles
        for iSugar in range(1, 101-(iCandy+iSprinkles)):
            counts['Sugar'] = iSugar
            counts['Chocolate'] = 100 - (iCandy+iSprinkles+iSugar)

            capacity = counts['Sugar']*3 - counts['Sprinkles']*3 - counts['Candy']
            durability = counts['Sprinkles']*3
            flavor = counts['Candy']*4 - counts['Chocolate']*2
            texture = counts['Chocolate']*2 - counts['Sugar']*3
            calories = 0

            score = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
            if score > high:
                high = score
                recipe = counts.copy()

print(high)
