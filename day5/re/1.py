import re

pat = '^h..l$'
stra = input("enter the string: \n")

res = re.match(pat, stra)

if res:
    print("right swipe")
else:
    print("no match")
