# files

#

fa = open("books.txt", "r")

lista = fa.readlines()
print(lista)

fb = open("books_new.txt", "w")

for val in lista[::2]:
    fb.write(val)

fa.close()
fb.close()

os.getcwd()
