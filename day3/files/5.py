# files

# internal cursor gets updated automatically
# 

fa = open("books.txt", "r")
stra = fa.read(5)
print(stra)
stra = fa.read(7)
print(stra)

print(fa.tell())

fa.seek(7)
print(fa.tell())
stra = fa.read(6)
print(stra)

fa.close()
