def if_a(stra):
    if 'a' in stra:
        return True

sa = ['brazil', 'peru', 'argentina', 'aruba', 'paraguay', 'chile']


res = []

for x in sa:
    if if_a(x):
       res.append(x)

print(res)
