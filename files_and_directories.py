"""
from pathlib import Path
path1=Path("ecommerce") 
path2=Path("ecommerce1") 
print(path1.exists()) #it will print a boolean
print(path2.exists()) #it will print a boolean it checks if there have any directory or not 
#to make a directory
path3=Path("extra")
#print(path3.mkdir()) # it will creat a directory 
#print(path3.rmdir()) #  it will delete the directory
"""
#print all python files from the directory
from pathlib import Path
path=Path()
for i in path.glob("*.py"):
    print(i)