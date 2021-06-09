def if_a(stra):
    if 'a' in stra:
        return True
    else:
        return False

sa = ['brazil', 'peru', 'argentina', 'aruba', 'paraguay', 'chile']

res = list(filter(if_a , sa))

print(res)
