import re

pat = '\d+'

rep = '##'

with open("data.txt", "r") as fa:
    stra = fa.read()

res = re.sub(pat, rep, stra)
print(res)

