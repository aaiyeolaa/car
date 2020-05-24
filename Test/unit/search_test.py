from unittest import TestCase
from search import Search


class SearchTest(TestCase):

    def test_create_search(self):
        s = Search('used')
        self.assertEqual('used', s.search_type)
        self.assertListEqual([], s.cars)

    def test_repr(self):
        s = Search("used")
        self.assertEqual(s.__repr__(), 'You have searched for 0 used car(s)')




