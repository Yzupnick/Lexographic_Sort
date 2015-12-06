import unittest
from lex import lex_sort

class TestStringMethods(unittest.TestCase):

    def test_returns_all_items(self):
        test1 = lex_sort(['abc','def'], 'abcdef')
        self.assertEqual(len(test1), 2)
        self.assertTrue('abc' in test1)
        self.assertTrue('def' in test1)

    def test_sorts_equal(self):
        test1 =   lex_sort(["acb", "abc", "bca"], "abc")
        self.assertEqual(len(test1), 3)
        self.assertEqual(test1[0], "abc")
        self.assertEqual(test1[1], "acb")
        self.assertEqual(test1[2], "bca")

    def test_sorts_same_char(self):
        test1 = lex_sort(["a", "aaa","", "aa"], "a")
        self.assertEqual(len(test1), 4)
        self.assertEqual(test1[0], "")
        self.assertEqual(test1[1], "a")
        self.assertEqual(test1[2], "aa")
        self.assertEqual(test1[3], "aaa")



if __name__ == '__main__':
    unittest.main()
