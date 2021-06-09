def func(stra):
    if 'a' in stra:
        return stra.replace('a', 'A')
    else:
        return stra.upper()

sa = ['brazil', 'peru', 'argentina', 'aruba', 'paraguay', 'chile']

res = list(map(func , sa))

print(res)


lista = [11, 21, 13, 10, 6, 5, 12, 14, 18, 23]
