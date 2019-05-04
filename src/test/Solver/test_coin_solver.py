'''
Created on May 4, 2019

@author: hlubyluk
'''
import unittest
from main.Solver import CoinSolver


class Test(unittest.TestCase):

    def test_coins1(self):
        self.assertEqual(10, CoinSolver([1, 2, 5], 10).solve())

    def test_coins2(self):
        self.assertEqual(29, CoinSolver([1, 2, 5], 20).solve())

    def test_coins3(self):
        self.assertEqual(40, CoinSolver([1, 2, 5, 10], 20).solve())

    def test_coins4(self):
        self.assertEqual(341, CoinSolver([1, 2, 5, 10], 50).solve())


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_coins']
    unittest.main()
