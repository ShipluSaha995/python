"""
import random
for i in range(3):
    print(random.random())
    """

#print random values between 10-20
"""
import random
for i in range(3):
    print(random.randint(10, 20))
"""

## pick a random name 
import random
#n=int(input("Enter how many names you want to give: "))
name=input("Enter names: ").split()
"""
for i in range(n):
    element=input().split()
    name.append(element)
"""

leader=random.choice(name)
print(leader)

