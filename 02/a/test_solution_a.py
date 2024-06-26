import unittest
from problem_a import solution

class TestProblemA(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solution('Sat', [5, 4, 3, 1, 1]), 25)

    def test_02(self):
        self.assertEqual(solution('Sat', [3, 1, 4, 1, 5]), 25)

    def test_03(self):
        self.assertEqual(solution('Thu', [0]), 32)

    def test_04(self):
        self.assertEqual(solution('Thu', [30]), 0)

    def test_05(self):
        self.assertEqual(solution('Fri', [31]), 31)

if __name__ == "__main__":
    unittest.main()
