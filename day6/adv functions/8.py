def func(a, b):
    return 2*a+3*b-10

def funcb(x):
    return 4*x**2 + 6*x + 10     # 4x2+6x+10

sa = ['brazil', 'peru', 'argentina', 'aruba', 'paraguay', 'chile']



lista = [11, 21, 13, 10, 6, 5, 12, 14, 18, 23]
listb = (17, 13, 41, 22, 8, 9, 17)


res = tuple(map(lambda a,b : 2*a+3*b-10 , lista, listb))
print(res)


res = list(filter( lambda x: 'a' in x , sa))
print(res)

