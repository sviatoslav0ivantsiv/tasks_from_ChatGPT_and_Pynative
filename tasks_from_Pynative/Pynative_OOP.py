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