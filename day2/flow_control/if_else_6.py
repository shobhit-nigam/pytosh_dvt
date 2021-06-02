# if else
# input 

# error 
age = eval(input("pleas enter the age: "))
print(type(age))

# may be error 
if age < 18:
    print("no vaccine")
    # code block
elif age >= 18 and age <45:
    print("difficult, but try to get vaccinated")
elif age > 45 and age < 60:
    print("should have been vaccinated by now")
elif age == 21:
    print("welcome to 20s")
else:
    print("senior citizens")
print("mask on")



