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
"""
#conditional operator
price=float(input())
good_credit=input() #take input True or False

if good_credit:
    down_payment=price*0.1
else:
    down_payment=price*0.2

print(f"down payment:${down_payment}")

"""
#comparision
"""
name=input()

if len(name)<3:
    print("Name must be at least 3 characters.\n")
elif len(name)>50:
    print("name can be a maximum of 50 characters.\n")
else:
    print(f'The name "{name}" looks good.\n')

"""
"""
weight=float(input("Enter Weight: "))
word=input("L(bs) or (k)g: ")

if word=="L" or word=="l":
    convertL=weight*0.45
    print(f'Your weight in kg : {convertL}\n')
elif word=="K" or word=="k":
    convert=weight/0.45
    print(f'Your weight in pounds: {convert}\n')
else:
    print("Invalid Choice.\n")
"""


#for loop
"""
number=input("enter numbes: ")
for i in number:
    print(i)
"""

#for loop
"""
for i in range(1, 10+1):
    print(i)
"""
#n=int(input("Enter the total number of items: "))
"""
price=input("Enter the prices: ").split()
total=0
for i in price:
    total=total+float(i)
print(f"Total Price: {total}\n")
"""
"""
numbers= input().split()
for num in numbers:
    i=int(num)
    output=""
    for j in range(i):
        output+='X'
    print(output)
"""

#find the maximum number from the list
n=int(input())
number=[]

for num in range(n):
    element=int(input())
    number.append(element)

maxi=number[0]
for i in number:
    if i>maxi:
        maxi=i

print(f'maximum:{maxi}')