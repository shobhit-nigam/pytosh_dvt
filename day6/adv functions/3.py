def func(la):
    if la>8 and la%3==0:
        return True
    else:
        return False

lista = [11, 21, 13, 10, 6, 5, 12, 14, 18, 23]

sa = ['brazil', 'peru', 'argentina', 'aruba', 'paraguay', 'chile']

res = list(filter(func , lista))

print(res)
