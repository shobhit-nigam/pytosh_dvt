# files

# with open (fetching the file to ram)
# auto close

with open("books.txt", "r") as fa:
    stra = fa.read()

print(stra)
