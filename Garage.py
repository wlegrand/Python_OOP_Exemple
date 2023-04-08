
class Garage:
    def __init__(self, location, max_cars):
        self.location = location
        self.max_cars = max_cars
        self.cars = []

    def add_car(self, voiture):
        if len(self.cars) < self.max_cars:
            self.cars.append(voiture)
            return True

        print("garage is full")
        return False
