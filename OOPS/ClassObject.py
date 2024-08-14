class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def start(self):
        print("Car started")

# Creating instances
car1 = Car("red", "Corolla", 2023)
car2 = Car("blue", "Camry", 2024)

# Accessing attributes and methods
print(car1.color)  # Output: red
print(car2.model)  # Output: Camry

car1.start()  # Output: Car started
