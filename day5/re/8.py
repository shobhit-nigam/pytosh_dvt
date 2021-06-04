import re

pat = '\d{2,4}'

pat = '\s+'
rep = '_'

with open("data.txt", "r") as fa:
    stra = fa.read()

res = re.sub(pat, rep, stra)
print(res)

