boss_hp = 100
boss_damage = 8
boss_armor = 2

weapons = {
    'Dagger': [8, 4, 0],
    'Shortsword': [10, 5, 0],
    'Warhammer': [25, 6, 0],
    'Longsword': [40, 7, 0],
    'Greataxe': [74, 8, 0],
}

armor = {
    'None': [0, 0, 0],
    'Leather': [13, 0, 1],
    'Chainmail': [31, 0, 2],
    'Splintmail': [53, 0, 3],
    'Bandedmail': [75, 0, 4],
    'Platemail': [102, 0, 5],
}

rings = {
    'Damage +0': [0, 0, 0],
    'Damage +1': [25, 1, 0],
    'Damage +2': [50, 2, 0],
    'Damage +3': [100, 3, 0],
    'Defense +0': [0, 0, 0],
    'Defense +1': [20, 0, 1],
    'Defense +2': [40, 0, 2],
    'Defense +3': [80, 0, 3],
}

player_hp = 100
winning_costs = set()
for w in weapons.keys():
    for a in armor.keys():
        for r1 in rings.keys():
            for r2 in rings.keys():
                cost = weapons[w][0] + armor[a][0] + rings[r1][0] + rings[r2][0]
                player_damage = weapons[w][1] + armor[a][1] + rings[r1][1] + rings[r2][1]
                player_armor = weapons[w][2] + armor[a][2] + rings[r1][2] + rings[r2][2]

                if ((boss_hp / max(1, (player_damage - boss_armor))) <= (player_hp / max(1, (boss_damage - player_armor)))):
                    winning_costs.add(cost)

print(min(winning_costs))
