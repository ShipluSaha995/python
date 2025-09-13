#Error handeling
"""
try:
    age=int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value\n")

"""

try:
    age=int(input("Age:" ))
    income=1000000
    #risk=income/0 ## it will give zero division error
    risk=income/age
    print(age)
    print(risk)
except ZeroDivisionError:
    print("Age can not be zero.\n")
except ValueError:
    print("Error\n")
