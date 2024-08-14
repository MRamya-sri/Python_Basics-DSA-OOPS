# Multiple Inheritance
# A derived class inherits from more than one base class.


class Parent1:
    def __init__(self):
        print("Parent1")

class Parent2:
    def __init__(self):
        print("Parent2")

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)

# Create an object of the Child class
child = Child()
