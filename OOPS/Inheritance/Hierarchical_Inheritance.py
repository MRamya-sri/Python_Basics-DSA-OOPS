class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Barking..")

class Cat(Animal):
    def meow(self):
        print("Meow!!")

## creating objects

objDog = Dog("Buddy")
objCat = Cat("Whiskey")

objDog.bark()
objCat.meow()