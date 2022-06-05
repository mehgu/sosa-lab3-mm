import unittest
from dodatak_A import OperationsManager


class TestOperationsManager(unittest.TestCase):

    def test_div_by_zero(self):
        a = 10.0
        b = 0.0
        om = OperationsManager(a, b)
        self.assertEqual(om.perform_division(), 0)

    def test_div_two_positives(self):
        a = 10.0
        b = 5.0
        om = OperationsManager(a, b)
        self.assertEqual(om.perform_division(), 2.0)


if __name__ == '__main__':
    unittest.main()
