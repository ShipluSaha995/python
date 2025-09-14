# class EmalClient # in class we have to capitalize the first letter of every letter.
"""
class Point:
    def move(self):
        print("move\n")
    def draw(self):
        print("draw")
    
point1=Point()
point1.draw()
point1.x=10
point1.y=20
print(point1.x, point1.y)
"""
#constructor
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

point=Point(10, 20)
print(point.x, point.y)