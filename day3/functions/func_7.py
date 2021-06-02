# functions
# global, local
ga = 33

def funca():
    print("inside ga = ", ga)
    la = 100
    print("inside la = ", la)

funca()

print("outside func, ga =", ga)
# error
print("outside la =", la)

