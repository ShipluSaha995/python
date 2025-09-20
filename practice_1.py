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
"""
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
"""

#list
"""
n=int(input())
numbers=[]
for num in range(n):
    element=int(input())
    numbers.append(element)

print(numbers)

print(numbers[0:2])
pos= int(input("Enter position: "))
el=int(input("enter element: "))
numbers.insert(pos, el)
print(numbers)

x=int(input("Enter a new list length: "))
new_num=[]
for i in range(x):
    new_element=int(input())
    new_num.append(new_element)

numbers.extend(new_num)
print(numbers)

y=int(input("Enter element to remove: "))
numbers.remove(y)
print(numbers)

numbers.pop()
print(numbers)

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
"""

#remove duplicstes
"""
n=int(input())
number=[]

for i in range(n):
    element=int(input())
    number.append(element)

unique=[]
for num in number:
    if num not in unique:
        unique.append(num)
print(unique)
"""
"""
phone=input("Phone Number: ")
number_maping={
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}

output=""
for i in phone:
    output+=number_maping.get(i, "!")+" "
print("\n")
print(output,"\n")
"""

#emoji converter

"""
message=input("Enter your massage: ")
words=message.split()

emoji={
    ":)":"😊",
    ":(":"😞"
}

output=""
for word in  words:
    output+=emoji.get(word, words)+" "
print(output)
"""
"""
class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print(f"Hi, I am {self.name}")
    def __str__(self):
        return(f"{self.name}")

# name=input("Enter name: ")
person=Person(input("Enter name: "))
person.talk()

"""
"""
def lb_to_kg(n):
    print(f"Your weight in kg: {n*0.48:.2f}")
def kg_to_lb(n):
    print(f"Your weight in pounds: {n/0.48:.2f}")

string=input("Enter your choice: ")
if string=='lb':
    n=float(input("Enter your weight(lb): "))
    kg_to_lb(n)

elif string=='kg':
    n=float(input("Enter your weight(kg): "))
    lb_to_kg(n)

else:
    print("invalid choice.")

"""
"""
#used for import this fuction to the modules file
def find_max(numbers):
    maximum=numbers[0]
    for i in numbers:
        if i>maximum:
            maximum=i
    return maximum
"""
"""
##Dice roll
import random
class Dice:
    def roll(self):
        first=random.randint(1, 6)
        second=random.randint(1, 6)
        return first, second

dice=Dice()
print(dice.roll())
"""

#simple calculator
print("\n\t\t\t Normal Calculator\n\t\t\t____________________\n\n")

print("1. Addition.\n2. Substraction.\n3. Multiplication.\n4. Division\n")
choice=int(input("Enter your choice: "))

if choice not in [1,2,3,4]:
    print("Invalid Choice")

else:
    
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    if choice==1:
        print(f"Result: {num1+num2}")

    elif choice==2:
        print(f"Result: {num1-num2}")

    elif choice==3:
        print(f"Result: {num1*num2}")

    elif choice==4:
        if num2!=0:
            print(f"Result: {num1/num2}")

        else :
            print("can not divided by zero it will bw an infinity.\n")

