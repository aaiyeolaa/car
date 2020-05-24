class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage_reading = 0

    def json(self):
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year
        }

    def get_car_description(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def check_light_type(self):
        if self.year >= 2015:
            return "Your car uses LED lights"
        elif self.year >= 2010:
            return "Your car uses XENON lights"
        else:
            return "Your car uses HALOGEN lights"

    def read_mileage(self):
        print(f"this car has a mileage of {self.mileage_reading} miles on it")

    def update_mileage(self, mileage):
        if mileage >= self.mileage_reading:
            self.mileage_reading = mileage
        else:
            print("You cannot roll back the mileage")

    def increment_mileage(self, mileage):
        self.mileage_reading += mileage



