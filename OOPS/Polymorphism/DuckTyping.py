# Duck Typing is like saying, "If it quacks like a duck, treat it like a duck." In Python, we don't check the exact type of an object. Instead, we check if it has the methods or attributes we need.

def make_sound(animal):
    animal.quick()

class Duck:
    def quick(self):
        print("Quick..")

class RobotDuck:
    def quick(self):
        print("Quick.. (Robot)")

# creating objects

duck = Duck()
robot = RobotDuck()  #these both are those "We can pass any object with a quack method to make_sound.""

# We have a make_sound function that expects an object with a quack method.
# Both Duck and RobotDuck classes have a quack method.
# We can pass any object with a quack method to make_sound.

make_sound(duck)
make_sound(robot)