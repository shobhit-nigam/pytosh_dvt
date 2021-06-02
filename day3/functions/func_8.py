# functions
# global, local
ga = 33
print("outside func, ga =", ga)
def funca():
    la = 100
    ga = 50
    print("inside la = ", la)
    print("inside ga = ", ga)

funca()

print("outside func, ga =", ga)

