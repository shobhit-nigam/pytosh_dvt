#  #  nesting

avengers = ['hulk', 'captain', 'ironman', 'captain', 'black widow']
dc = ['wonderwoman', 'batman', 'joker', 'aquaman']

heroes = ['shaktiman', 'asterix', 'omniman', avengers, dc]

print("heroes = ", heroes)
#print("type of heroes = ", type(heroes))
#print("type of heroes[2] = ", type(heroes[2]))
#print("type of heroes[3] = ", type(heroes[3]))
print("heroes[3][3][3] =", heroes[3][3][3])
