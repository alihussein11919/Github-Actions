import unittest

# Function we want to test
def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# Test case class
class TestMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertAlmostEqual(divide_numbers(7, 3), 2.3333, places=4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide_numbers(5, 0)

# Run tests
if __name__ == '__main__':
    unittest.main()

