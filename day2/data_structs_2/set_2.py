# set

fruits = {'plums', 'apples', 'oranges', 'plums', 'grapes', 'oranges', 'pears'}
baskets = {'oranges', 'melons', 'grapes', 'guavas', 'bananas'}

print("baskets =", baskets)
print("fruits =", fruits)

print(fruits & baskets)         # & intersection 
print(fruits | baskets)         # pipe union
print(fruits ^ baskets)         # uncommon, symmetric differnece
print(fruits - baskets)         # difference



