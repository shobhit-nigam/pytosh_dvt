# for using range with start & end
# increment in form steps

lista = ['rr', 'yy', 'tt', 'll', 'ee', 'yy', 'ff', 'ss', 'yy']

index = []

for i in range(len(lista)):
    if lista[i] == 'yy':
        index.append(i)

print("'yy' occurs at indexes --> ", index)
        
    
               

