from car import Car


class Search:
    def __init__(self, search_type):
        self.search_type = search_type
        self.cars = []

    def __repr__(self):
        return 'You have searched for {} {} car(s)'.format(len(self.cars),
                                                           self.search_type)

    def add_car_search_to_list(self, make, model, year):
        self.cars.append(Car(make, model, year))

    def json(self):
        return dict(search_type=self.search_type, cars=[car.json() for car in self.cars])
