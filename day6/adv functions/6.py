def func(a, b):
    return 2*a+3*b-10

sa = ['brazil', 'peru', 'argentina', 'aruba', 'paraguay', 'chile']



lista = [11, 21, 13, 10, 6, 5, 12, 14, 18, 23]
listb = (17, 13, 41, 22, 8, 9, 17)


res = tuple(map(func , lista, listb))

print(res)
