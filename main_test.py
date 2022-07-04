from unittest import TestCase, main
from random import randint
from main import switch_case, get_result

class CalculatorTest(TestCase):
    def test_plus(self):
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        self.assertEqual(get_result(operator_func = switch_case(operator = "+"), num_1 = num_1, num_2 = num_2), float(num_1 + num_2))

    def test_minus(self):
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        self.assertEqual(get_result(operator_func = switch_case(operator = "-"), num_1 = num_1, num_2 = num_2), float(num_1 - num_2))

    def test_multy(self):
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        self.assertEqual(get_result(operator_func = switch_case(operator = "*"), num_1 = num_1, num_2 = num_2), float(num_1 * num_2))

    def test_divide(self):
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        self.assertEqual(get_result(operator_func = switch_case(operator = "/"), num_1 = num_1, num_2 = num_2), float(num_1 / num_2))

    def test_zero_division(self):
        self.assertEqual(get_result(operator_func = switch_case(operator = "/"), num_1 = 0, num_2 = 0), None)

if __name__ == "__main__":
    main()
