import unittest
from math_quiz import generate_function_integer, generate_random_operator, result


class TestMathGame(unittest.TestCase):

    def test_generation_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_function_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if generated operator is one of '+', '-', '*'
        operators = {'+', '-', '*'}
        for _ in range(1000):
             select_operator = generate_random_operator()
             self.assertIn(select_operator,operators)

    def test_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                test_calculate = result(num1, num2, operator)
                self.assertEqual(test_cases,test_calculate)

if __name__ == "__main__":
    unittest.main()
