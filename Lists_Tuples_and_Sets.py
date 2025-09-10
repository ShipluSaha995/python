#lists
"""

course=['History', 'Physics', 'Math', 'CSE', 'ML']
print(course,"\n")
print(course[0:2], "\n")
print(course[2:], "\n")

course.insert(0, 'AI') #this inserrt function is use to add an element in a requiered index 
print(course, "\n")

course_2=['CSE 205', 'CSE 206']
course.extend(course_2)  #this extend function used to concat 2 lists  
print(course, "\n")

course.append(course_2) # append is use to add a list in a list 
print(course, "\n") 

course.remove("History") #remove function deletes the element you wanted to delete from the list
print(course)

course.pop()  #pop function deletes the last element from the list
print(course, "\n")


#to take user input in list
"""
"""
n=int(input())
string=[]

for i in range(n):
    element=input().split()
    string.append(element)

print(string)

"""
"""
course.reverse() #to reverse the list
print(course)

n=int(input())
string=[]

for i in range(n):
    element=input()
    string.append(element)

print(string)

string.sort() # to sort the elements in the list in aecending order
print(string)

string.sort(reverse=True) #to sort elements in decending order
print(string)

sorted_courses=sorted(course) # to get the sorted version of that list in this we ahve to use a variable 
print(course)

print(max(string)) #to get the maximum value of the list
print(min(string)) # to get the minimum value
print(course.index('CSE 205')) # to get the index number of that element

new=['A', 'B', 'c']
st=", ".join(new) #we can also use .split()
print(st)
"""
"""
"""
# tuple
# tuples are immutable we can not change them
"""
tuple_1=('math', 'science', 'history')
tuple_2=tuple_1
tuple_1[0]='Art' # we can't change it will give an error
print(tuple_1)
print(tuple_2)
"""

#sets
#sets removes duplicates and it doesn't care about orders
course={'Arts', 'science', 'history', 'bng'}
course2={'Arts', 'science', 'physics', 'bio'}
print(course)
print(course.intersection(course2)) #print the smillar values between both sets
print(course.difference(course2)) #print the different values between both sets
print(course.union(course2)) #add both the list together

"""
# to creat empty list
empty_list=[]
empty_list=list()

# to creat empty tuple
empty_tuple=()
empty_tuple=tuple()

# to creat empty set
empty_set=set()
"""

