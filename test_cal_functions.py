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


if __name__ == '__main__':
    unittest.main()



