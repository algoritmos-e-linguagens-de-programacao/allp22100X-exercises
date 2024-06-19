import unittest
from problem_b import solution

class TestSolution(unittest.TestCase):
    def test_single(self):
        trips = [
            ['Y', 'N'],
            ['N', 'N'],
            ['Y', 'N'],
            ['N', 'Y'],
            ['Y', 'Y']
        ]
        output = [
            ['Y', 'N'],
            ['N', 'N'],
            ['Y', 'Y'],
            ['N', 'Y'],
            ['Y', 'Y']
        ]
        self.assertEqual(solution(5, 2, 1, trips), output)

if __name__ == "__main__":
    unittest.main()
