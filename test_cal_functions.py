"""test module for cal functions"""

# imports
import unittest         # required for testing
import cal_functions    # module under test


class TestCalFunctions(unittest.TestCase):
    """class to test functions in cal functions"""

    def test_add(self):
        """add function test"""
        self.assertEqual(cal_functions.add(10, 5), 15)
        self.assertEqual(cal_functions.add(-1, -1), -2)
        self.assertEqual(cal_functions.add(-5, 7), 2)

    def test_subtract(self):
        """add function test"""
        self.assertEqual(cal_functions.subtract(10, 5), 5)
        self.assertEqual(cal_functions.subtract(-1, -1), 0)
        self.assertEqual(cal_functions.subtract(-5, 7), -12)

    def test_multiply(self):
        """add function test"""
        self.assertEqual(cal_functions.multiply(10, 5), 50)
        self.assertEqual(cal_functions.multiply(-1, -1), 1)
        self.assertEqual(cal_functions.multiply(-5, 7), -35)

    def test_divide(self):
        """add function test"""
        self.assertEqual(cal_functions.divide(10, 5), 2)
        self.assertEqual(cal_functions.divide(-1, -1), 1)
        self.assertEqual(cal_functions.divide(-5, -5), 1)

        with self.assertRaises(ValueError):
            cal_functions.divide(5, 0)


if __name__ == '__main__':
    unittest.main()



