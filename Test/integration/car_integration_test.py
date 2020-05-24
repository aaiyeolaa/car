from unittest import TestCase
from car import Car


class CarIntegrationTest(TestCase):

    def test_update_mileage(self):
        car = Car('Audi', 'A5', 2017)
        current = car.update_mileage(10000)
        self.assertEqual(current, car.read_mileage())
