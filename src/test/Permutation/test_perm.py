'''
Created on Mar 31, 2019

@author: hlubyluk
'''
import unittest
from main.Permutation import *


class Test(unittest.TestCase):

    def setUp(self):
        self.perm = Permutation()

    def tearDown(self):
        del(self.perm)

    def test_perm_ok(self):
        a = [0, 1, 2, 5, 3, 3, 0]
        self.perm.next_lexigonal_permutation(a)
        b = [0, 1, 3, 0, 2, 3, 5]
        self.assertListEqual(b, a)

    def test_perm_ko(self):
        a = [0, 1, 2, 5, 3, 3, 0]
        b = a
        self.perm.next_lexigonal_permutation(a)
        self.assertEqual(b, a)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
