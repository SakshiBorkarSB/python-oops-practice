import math

class Shape:
    def area(self):
        print("Area: ")
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
c1 = Circle(1)
r1 = Rectangle(1, 1)
t1 = Triangle(1, 1)

print("Area of Circle", c1.area())
print("Area of Rectangle:", r1.area())
print("Area of Traingle:", t1.area())
