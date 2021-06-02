# if else
# input 

# nesting
age = eval(input("please enter the age: "))
gender = input("please enter the gender: ")

# may be error 
if age < 18:
    print("no vaccine")
    # code block
elif age >= 18 and age <45:
    print("difficult, but try to get vaccinated")
elif age > 45 and age < 60:
    print("should have been vaccinated by now")
    if gender == 'm':
        print("no discounts")
    elif gender == 'f' or gender == 'o':
        print("10% discounts")
elif age == 21:
    print("welcome to 20s")
else:
    print("senior citizens")
print("mask on")



