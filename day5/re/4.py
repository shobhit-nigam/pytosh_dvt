import re

pat = 'h..l'

#pat = '\d{2,4}'

with open("data.txt", "r") as fa:
    stra = fa.read()

res = re.findall(pat, stra)
print(res)

