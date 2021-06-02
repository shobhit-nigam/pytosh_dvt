# files

# open (fetching the file to ram)
fa = open("books.txt", "r")

# reading 5  bytes
stra = fa.read(5)

print(stra)

fa.close()
