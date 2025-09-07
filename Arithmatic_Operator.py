#Arithmetic Operators

"""
Addition -> +
substractio -> -
multiplicatio -> *
division -> /
Modulus -> %
Exponent -> **
Floor Division -> //

"""
"""
num1=int(input())
num2=int(input())

sum=num1+num2
sub=(num1-num2)
div=(num1/num2)
mul=(num1*num2)
exp=(num1**num2)
fl=num1//num2

num1+=10

print(sum, sub, mul, div, exp, fl, num1,"\n")
print((3+2)*5-1)

print(round(2.5))
print(round(3.75, 1))
print(abs(-2.5))

"""

#import math
#print(math.ceil(2.9))


"""
comparisons:
equal -> ==
nor equal -> !=
grater than -> 3>2
less than -> 3<2
grater or equal -> 3>=2
less or equal -> 3<=2
"""
"""
temp=float(input())
if temp>30:
    print("Its a hot day.\n")
elif temp<10:
    print("Its a cold day.\n")
else:
    print("It's neither hot or cold.\n")
"""