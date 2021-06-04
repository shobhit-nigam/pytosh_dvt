import re

pat = '\d+'

pat = '\d{3}'

with open("data.txt", "r") as fa:
    stra = fa.read()

res = re.findall(pat, stra)
print(res)

