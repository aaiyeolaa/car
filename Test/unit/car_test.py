from typing import Dict, Union
from unittest import TestCase
from car import Car


class CarTest(TestCase):
    def test_create_car(self):
        car = Car('Audi', 'A5', 2017)
        self.assertEqual('Audi', car.make)

    def test_car_json(self):
        car = Car('Audi', 'A5', 2017)
        expected = {'make': 'Audi', 'model': 'A5', 'year': 2017}
        self.assertDictEqual(expected, car.json())

    def test_get_car_description(self):
        car = Car('Audi', 'A5', 2017)
        self.assertEqual('2017 Audi A5', car.get_car_description())

    def test_car_headlight_type(self):
        car1 = Car('Audi', 'A5', 2017)
        car2 = Car('VW', 'Golf', 2013)
        car3 = Car('Mercedes', 'E-200 V-Booth', 1985)
        self.assertEqual(car1.check_light_type(), "Your car uses LED lights", "wrong light option")
        self.assertEqual(car2.check_light_type(), "Your car uses XENON lights", "wrong light option")
        self.assertEqual(car3.check_light_type(), "Your car uses HALOGEN lights", "wrong light option")







