
class Garage:
    def __init__(self, location, max_cars):
        self.location = location
        self.max_cars = max_cars
        self.cars = []

    def add_car(self, voiture, max_cars):
        if len(self.cars) < self.max_cars:
            self.cars.append(voiture)
            return True

        print("garage is full, there's only", max_cars, "places")
        return False
