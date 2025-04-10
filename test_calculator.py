import unittest, calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(3, 5), 8)
        self.assertEqual(calculator.add(-5, 6), 1)
        self.assertEqual(calculator.add(-8, -6), -14)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(5, 4), 1)
        self.assertEqual(calculator.subtract(-5, 4), -9)
        self.assertEqual(calculator.subtract(-5, -4), -1)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(0, 99), 0)
    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5.0)
        self.assertEqual(calculator.divide(4, -8), -2.0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.log(10, 100), 2)
        self.assertEqual(calculator.log(10, 10), 1)
        self.assertEqual(calculator.log(100, 10), 0.5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(-10, -100)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -100)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(2), 2 ** 0.5)
        self.assertIsNone(calculator.square_root(-4))  # Based on try/except return None

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()