import unittest
from finite_automata import KMP

class TestKMPMethods(unittest.TestCase):

    def test_search(self):
        kmp = KMP("abc")
        self.assertEqual(kmp.search("abcabcabc"), [0, 3, 6])
        self.assertEqual(kmp.search("abcdabcabc"), [0, 4, 7])

if __name__ == '__main__':
    unittest.main()
