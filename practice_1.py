#take user input  name and his favourite color and print them
"""
name=input("What is your name?\n")
print("Hi "+name)
color=input("What is your fovourite color?\n")
print(name +" likes "+color+"\n")
"""
# Type conversition
"""
birth_year=int(input("Your birth year: "))
Running_year=int(input("Running Year: "))
age=Running_year - birth_year
print("Your age is: ", age)


weight=float(input("Enter your weight(lbs): "))
convert=float(weight*0.453592)
print("Your weight in kilogram is: ", convert)

"""

#conditional operator
price=float(input())
good_credit=input() #take input True or False

if good_credit:
    down_payment=price*0.1
else:
    down_payment=price*0.2

print(f"down payment:${down_payment}")


