coustomer={
    "Name":"John Smith",
    "Age":"30",
    "is_verified": True
}

print(coustomer["Name"])
print(coustomer["Age"])

#we can also use get
print(coustomer.get("Name"))
print(coustomer.get("Age"))
print(coustomer.get("Birth_Date")) #here we will get None if we dont use get it will give an error
