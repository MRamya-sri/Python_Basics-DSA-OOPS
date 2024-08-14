## Single Inheritance
## A derived class inherits from only one base class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal Speaking..")

class Dog(Animal):
    def bark(self):
        print("Animal Barking..")

# creating an object of the Dog class
objDog = Dog("Doggy")
objDog.speak()
objDog.bark()
