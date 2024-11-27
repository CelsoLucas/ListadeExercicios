import os
from Car import Car
from Motorcycle import MotorCycle
from Truck import Truck

os.system("cls")

print("Car")
brand = str(input("Brand: "))
model = str(input("Model: "))
car1 = Car(brand, model)
car1.fuel_type()
car1.passenger_capacity()

os.system("cls")

print("MotorCycle")
brand = str(input("Brand: "))
model = str(input("Model: "))
motorcycle1 = MotorCycle(brand, model)
motorcycle1.fuel_type()
motorcycle1.passenger_capacity()

os.system("cls")

print("Truck")
brand = str(input("Brand: "))
model = str(input("Model: "))
truck1 = Truck(brand, model)
truck1.fuel_type()
truck1.passenger_capacity()

os.system("cls")

print("Car")
print(f"Brand: {car1.brand} | Model: {car1.model} | Fuel Type: {car1.type_fuel} | Passanger Capacity: {car1.pass_cap}")
print("=-="*15)
print("MotorCycle")
print(f"Brand: {motorcycle1.brand} | Model: {motorcycle1.model} | Fuel Type: {motorcycle1.type_fuel} | Passanger Capacity: {motorcycle1.pass_cap}")
print("=-="*15)
print("Truck")
print(f"Brand: {truck1.brand} | Model: {truck1.model} | Fuel Type: {truck1.type_fuel} | Passanger Capacity: {truck1.pass_cap}")
print()