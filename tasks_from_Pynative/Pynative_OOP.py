# pynative OOP Exercise 1:
#
# class Vehicle :
#     def __init__(self, max_speed, mileage ):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# modelS1 = Vehicle(300, 200)
#
# print(modelS1.max_speed, modelS1.mileage)
import math


# pynative OOP Exercise 2:
# class Vehicle:
#     pass

# pynative OOP Exercise 3:
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#
#     def print_info(self):
#         print( f"Vehicle is {self.name}, his max speed is {self.max_speed}, and mileage is {self.mileage}")
# SchoolBus = Bus("School Volvo", 180, 12)
# SchoolBus.print_info()

# pynative OOP Exercise 4: Class Inheritance:
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
# # SameVehicle = Vehicle("Same Vehicle", 40000, 1000)
# # print(SameVehicle.seating_capacity(100))
# class Bus(Vehicle):
#     def seating_capacity(self, capacity = 50):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# SameBus = Bus("Bus", 180, 12)
# print(SameBus.seating_capacity())


# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.color = 'White'
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     def bus_info(self):
#         print( f"Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")
#
# class Car(Vehicle):
#     def cur_info(self):
#         print(f"Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")
#
# bus = Bus("Volvo", 180, 12)
# car = Car("Audi Q5", 240, 18)
#
# bus.bus_info()
# car.cur_info()


# OOP Exercise 6: Class Inheritance
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10/100
#         return amount
#
# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare() )
#


# OOP Exercise 7: Check type of an object
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
#
# School_bus = Bus("School Volvo", 12, 50)
# print (type(School_bus))


# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)
#
# print(isinstance(School_bus, Vehicle)) #True
# print(isinstance(Bus, Vehicle)) #False
# print(issubclass(Bus, Vehicle)) #True Підклас

# OOP Exercise 9: Check object is a subclass of a particular class
# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# class Puppy(Dog):
#     pass
#
# class Cat:
#     pass
#
# print(issubclass(Dog, Animal))
# print(issubclass(Animal, Dog))
# print(issubclass( Cat, Animal))
# print(issubclass(Puppy, Animal))

# OOP Exercise 10: Calculate the area of different shapes using OOP
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    import math
    def area(self):
        return math.pi * math.pow(self.radius, 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    import math
    def area(self):
        return math.pow(self.side, 2)

# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())  # Output: 78.53975, 49, 28.27431