import re

pat = '\d+'

rep = '##'

with open("data.txt", "r") as fa:
    stra = fa.read()

res = re.subn(pat, rep, stra)
print(res)

