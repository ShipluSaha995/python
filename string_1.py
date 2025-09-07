print("hello world")
massage='hello WORLD'
print(massage)
print("length of the str=", len(massage)) #len used to find the length of the string
print(massage[4]) #finds the 4th index of the string 
print(massage[0:3])#prints the 1st to 3rd element from the string
print(massage[:3])# same like the previous one  

new="SHIPLU"
print(new.lower()) #to print the string in all lower case
up="shiplu"
print(up.upper()) #to print the string in all upper case

count="ikhfsdosohf opsidfhhdf sadpfh"
print(count.count('i'))  #to count the character want to count that how many times it exists in the string.  
print(massage.find('WORLD'))  #to find a character


##replacement in string
# massage=massage.replace("WORLD", "Universe")
print(massage.replace("WORLD", "Universe"))

#string concat

first="Hello"
second="Adam"

new_massage=first+", "+second+" "+"Welcome"
print(new_massage)

new_mas="{}, {}. Welcome!." . format(first, second)
print(new_mas)

new_mas=f"{first}, {second}. Welcome!.\n"
print(new_mas)

print(help(str))sssss