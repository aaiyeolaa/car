from unittest import TestCase
from unittest.mock import patch

import app
from search import Search


class AppTest(TestCase):
    def test_print_cars(self):
        pass

    def test_calling_builtin_print_in_print_cars(self):
        with patch('builtins.print') as mocked_print:
            s = Search('used')
            s.add_car_search_to_list('Audi', 'A5', 2015)
            app.searched_cars = {'Test': s}
            app.print_cars()
            mocked_print.assert_called_with('You have searched for 1 used car(s)')

    def test_calling_input_function(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.USER_PROMPT)

    def test_calling_print_cars(self):
        with patch('app.print_cars') as mocked_print_cars:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_cars.assert_called()

    def test_create_a_search(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = 'used'
            app.create_a_search()
            self.assertIsNotNone(app.searched_cars)



