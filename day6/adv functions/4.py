def func(stra):
    if 'a' in stra:
        return False
    else:
        return True

sa = ['brazil', 'peru', 'argentina', 'aruba', 'paraguay', 'chile']

res = list(filter(func , sa))

print(res)


lista = [11, 21, 13, 10, 6, 5, 12, 14, 18, 23]
