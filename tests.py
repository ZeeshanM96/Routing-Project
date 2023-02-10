import unittest

from main import get_best_operator


class TestGetBestOperator(unittest.TestCase):
    def setUp(self):
        self.operators = [
            {'1': 0.9, '268': 5.1, '46': 0.17, '4620': 0.0, '468': 0.15, '4631': 0.15, '4673': 0.9, '46732': 1.1},
            {'1': 0.92, '44': 0.5, '46': 0.2, '467': 1.0, '48': 1.2}
        ]

    def test_number_with_prefix_in_multiple_operators(self):
        number = '46732123456'
        result = get_best_operator(number, self.operators)
        self.assertEqual(result, ({'1': 0.9, '268': 5.1, '46': 0.17, '4620': 0.0, '468': 0.15, '4631': 0.15, '4673': 0.9, '46732': 1.1}, 1.1, '46732'))

    def test_number_with_prefix_in_single_operator(self):
        number = '468123456'
        result = get_best_operator(number, self.operators)
        self.assertEqual(result, ({'1': 0.9, '268': 5.1, '46': 0.17, '4620': 0.0, '468': 0.15, '4631': 0.15, '4673': 0.9, '46732': 1.1}, 0.15, '468'))

    def test_number_with_no_prefix(self):
        number = '987654321'
        result = get_best_operator(number, self.operators)
        self.assertEqual(result, (None, float('inf'), None))

    def test_multiple_operators(self):
        number = '46732'
        result = get_best_operator(number, self.operators)
        self.assertEqual(result, ({'1': 0.9, '268': 5.1, '46': 0.17, '4620': 0.0, '468': 0.15, '4631': 0.15, '4673': 0.9, '46732': 1.1}, 1.1, '46732'))

    def test_empty_operators_list(self):
        number = '46732123456'
        result = get_best_operator(number, [])
        self.assertEqual(result, (None, float('inf'), None))

if __name__ == '__main__':
    unittest.main()
