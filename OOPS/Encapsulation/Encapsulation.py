# Encapsulation is a fundamental OOP concept that involves bundling data (attributes) and the methods (functions) that operate on that data within a single unit, called a class. 
# It's like a capsule containing everything needed for a specific task. 
# The primary goal is to protect data integrity by controlling access to it.

# The Car as an Object
# A car is a perfect example of encapsulation. It has:

# Attributes: Color, model, engine type, fuel level, etc. These are like the data inside the car.
# Methods: Start, stop, accelerate, brake, etc. These are the actions the car can perform.


class Car:
    def __init__(self, color, model, engine):
        self.__color = color
        self.__model = model
        self.__engine = engine
        self.__fuel_level = 100

    def start(self):
        print("Car is starting..")

    def stop(self):
        print("Car Stopped!!")

    def accelerate(self):
        if self.__fuel_level > 0:
            print("Car Accelerating.....")
            self.__fuel_level -= 10
    
    def get_fuel_level(self):
        return self.__fuel_level
    
    def get_color(self):
        return self.__color
    
    def get_model(self):
        return self.__model
    
    def get_engine(self):
        return self.__engine
    
## creating object

objCar = Car("red", "swift", "electric")
print("Car Color:", objCar.get_color())
print("Car Model:", objCar.get_model())
print("Car Engine:", objCar.get_engine())

objCar.start()
objCar.accelerate()
print("Fuel Level:", objCar.get_fuel_level())

objCar.stop()