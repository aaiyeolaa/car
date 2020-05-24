from unittest import TestCase
from search import Search


class SearchIntegrationTest(TestCase):
    def test_single_car_search(self):
        s = Search('new')
        s.add_car_search_to_list('Audi', 'A5', 2019)
        self.assertEqual(len(s.cars), 1)
        self.assertEqual(s.__repr__(), 'You have searched for 1 new car(s)')

    def test_multiple_car_search(self):
        s = Search('used')
        s.add_car_search_to_list('Bentley', 'Mulsanne', 2010)
        s.add_car_search_to_list('Bentley', 'GT-Continental', 2010)
        self.assertEqual(len(s.cars), 2)
        self.assertEqual(s.__repr__(), 'You have searched for 2 used car(s)')

    def test_json(self):
        s = Search('used')
        s.add_car_search_to_list('Audi', 'A5', 2019)
        expected = dict(search_type='used', cars=[{'make': 'Audi', 'model': 'A5', 'year': 2019}])
        self.assertDictEqual(expected, s.json(), 'Dictionaries do not match')

    def test_json(self):
        s = Search('used')
        s.add_car_search_to_list('Audi', 'A5', 2019)
        s.add_car_search_to_list('Mercedes', 'C63 AMG', 2018)
        expected = {'search_type': 'used', 'cars': [{'make': 'Audi', 'model': 'A5', 'year': 2019},
                                                    {'make': 'Mercedes', 'model': 'C63 AMG', 'year': 2018}]}
        self.assertDictEqual(expected, s.json(), 'Dictionaries do not match')

