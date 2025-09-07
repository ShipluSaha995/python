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
## A car game just using command 
command=""
started=False

while True:
    command=input("Enter your comand: ")
    if command=="start":
        if started:
            print("The car is already started...\n")
        else:
            started=True
            print("Car Started.....\n")

    elif command=="stop":
        if not started:
            print("The car is already stopped.\n")
        else:
            started=False
            print("Car Stopped.\n")
        

    elif command=="help":
        print("""
        start -> to start the car
        stop -> to stop the car
        exit -> to exit  
        """)

    elif command=="exit":
        print('Exiting..')
        break

    else:
        print("Sorry, invalid command")
        break
