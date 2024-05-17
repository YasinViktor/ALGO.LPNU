# test.py

import unittest
from flood_fill import flood_fill

class TestFloodFill(unittest.TestCase):
    def test_flood_fill(self):
        test_cases = [
            {
                "input": (5, 5, 2, 2, 'B', ['AAAAA', 'AAAAA', 'AAAAA', 'AAAAA', 'AAAAA']),
                "output": ['BBBBB', 'BBBBB', 'BBBBB', 'BBBBB', 'BBBBB']
            },
            {
                "input": (5, 5, 0, 0, 'C', ['BBBBB', 'BAAAAB', 'BAAAAB', 'BAAAAB', 'BBBBB']),
                "output": ['CCCCC', 'CAAAAC', 'CAAAAC', 'CAAAAC', 'CCCCC']
            },
            {
                "input": (6, 6, 3, 3, 'D', ['CCCCCC', 'CBBBBBC', 'CBAAABC', 'CBAAABC', 'CBBBBBC', 'CCCCCC']),
                "output": ['CCCCCC', 'CBBBBBC', 'CBDDBBC', 'CBDDBBC', 'CBBBBBC', 'CCCCCC']
            }
        ]

        for test_case in test_cases:
            row, col, start_x, start_y, new_color, image = test_case["input"]
            expected_output = test_case["output"]
            result = flood_fill(row, col, image, start_x, start_y, new_color)
            self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
