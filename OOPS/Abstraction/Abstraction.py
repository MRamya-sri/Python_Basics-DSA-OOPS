from abc import ABC, abstractmethod

# abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

#Sub Classes to implement abstract methods.

#1st SubClass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2* self.length * self.width
    
#2nd subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
# creating an Object
obj = Rectangle(72, 45)
print(obj.area())
print(obj.perimeter())

    
        

