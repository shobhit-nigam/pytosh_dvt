# files

# open (fetching the file to ram)
fa = open("books.txt", "r")

# reading the entire file
stra = fa.read()

print(stra)

fa.close()
