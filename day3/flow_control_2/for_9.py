# for (dict)

lista = ['rr', 'yy', 'tt', 'll', 'ee', 'yy', 'ff', 'ss', 'yy']

num = 0

for val in lista:
    num = num+1
    if val == 'ee':
        print("found it")
        break


print("for ran", num, "times")
    
