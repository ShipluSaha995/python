#While loop
"""
i=1
while i<=5:
    print(' *'*i)
    i+=1
"""
"""
string=input("\ninput the string that you want to print: ")
i=1
end=int(input("\nHow many times do you want to print : "))

while(i<=end):
    print(f"{i}. {string}")
    i+=1
    
"""

#For loop
# for item in "python":
#     print(item)


"""
price=[]
n=int(input("Enter how many items do you have: "))

for i in range(n):
    element=float(input("Enter the price: "))
    price.append(element)
print(price)

total=0
for p in price:
    total += p
print(f"total ammount is: {total}")
"""

#nasted for loop
"""
for i in range(4):
    for j in range(3):
        print(f'({i}, {j})')
"""
"""
numbers=input().split()
for i in numbers:
    print('x'*int(i)) 
"""

#break statement
"""
for i in range(12):
     if i==10:
        break
     print('5 X', i+1, "=", 5*(i+1))
"""

#continue
for i in range(1, 6):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)
