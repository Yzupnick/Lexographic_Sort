import unittest
from lex import lex_sort

class TestStringMethods(unittest.TestCase):

  def test_returns_all_items(self):
      test1 = lex_sort(['abc','def'], 'abc')
      self.assertEqual(len(test1), 2)
      self.assertTrue('abc' in test1)
      self.assertTrue('def' in test1)


if __name__ == '__main__':
    unittest.main()
