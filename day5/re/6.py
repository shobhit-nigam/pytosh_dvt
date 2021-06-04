import re

pat = '\d{2,4}'

pat = '\s'

with open("data.txt", "r") as fa:
    stra = fa.read()

res = re.split(pat, stra, 5)
print(res)

