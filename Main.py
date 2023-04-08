from Cars import Cars
from Garage import Garage

num_cars = int(input("Enter the number of cars you want to add: "))

cars_list = []

for i in range(num_cars):
    brand = input("Enter the car brand: ")
    color = input("Enter the car color: ")
    power = int(input("Enter the car power: "))
    model = input("Enter the car model: ")

    car = Cars(brand, color, power, model)
    cars_list.append(car)

location = input("Enter the location of the garage: ")

max_cars = int(input("Enter the maximum number of cars the garage can hold: "))

garage = Garage(location, max_cars)

for car in cars_list:
    garage.add_car(car)

for i, car in enumerate(garage.cars):
    print("Car", i + 1)
    print("Brand:", car.brand)
    print("Color:", car.color)
    print("Power:", car.power)
    print("Model:", car.model)

print("The garage is in", garage.location, "and he has", garage.max_cars, "places")
