"""test module for car class"""

# imports
import unittest
from car import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car1 = Car('accord', '2008', 'black', 5000)
        self.car2 = Car('bmw', '2018', 'blue', 45000)

    def tearDown(self):
        pass

    def test_make_model_statement(self):

        self.assertEqual(self.car1.make_model_statement, 'accord of 2008 is the best car ever made')
        self.assertEqual(self.car2.make_model_statement, 'bmw of 2018 is the best car ever made')

        self.car1.model_name = 'Honda'     # the car1 assert statement should change

        self.assertEqual(self.car1.make_model_statement, 'Honda of 2008 is the best car ever made')

    def test_model_color_available(self):

        self.assertEqual(self.car2.model_color_available, 'bmw is available in blue color')


if __name__ == '__main__':
    unittest.main()


