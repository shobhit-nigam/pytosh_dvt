lista = ['tt', 'yy', 'rr', 'ww', 'xx', 'uu']

try:
    i = int(input("enter the index:\n"))
    print("lista[i] =", lista[i])
except IndexError:
    print("wrong index entered, defaulting to zero")
    i = 0
    print("lista[i] =", lista[i])
except ValueError:
    print("should have ntered only integers, defaulting to zero")
    i = 0
    print("lista[i] =", lista[i])
print("code continues")
