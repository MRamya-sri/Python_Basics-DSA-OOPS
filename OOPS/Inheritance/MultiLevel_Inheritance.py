# Multilevel Inheritance
# A derived class inherits from a base class, which in turn inherits from another base class.

class Grandfather:
    def __init__(self, name):
        self.name = name

class Father(Grandfather):
    def __init__(self, name, occupation):
        super().__init__(name)
        self.occupation = occupation

class Son(Father):
    def __init__(self, name, occupation, age):
        super().__init__(name, occupation)
        self.age = age

# Create an object of the Son class
son = Son("Rohan", "Engineer", 25)
print(son.name, son.occupation, son.age)
