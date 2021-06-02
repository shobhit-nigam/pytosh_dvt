# for (dict)

lista = ['rr', 'yy', 'tt', 'll', 'ee', 'yy', 'ff', 'ss', 'yy']
listb = ['tt', 'yy', 'qq', 'xx', 'jj', 'ss', 'll']

common = []
common_set = set()      # {}

for val in lista:
    if val in listb:
        common.append(val)
        common_set.add(val)


print("the common elements are =", common)
print("the common elements are =", common_set)
    
