#lists
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