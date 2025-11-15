'''
import my_moduls as mm

course=["phy", "math", "computer Sci"]
index= mm.find_index(course, "math")
print(index)
'''

#we can also do

from my_moduls import find_index
course=["phy", "math", "computer Sci"]
index= find_index(course, "math")
print(index)