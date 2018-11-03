'''
Created on Nov 3, 2018

@author: HlubyLuk
'''
import unittest
from euler.euler import Problem1, Problem2, Problem3, Problem4, Problem5


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProblem1(self):
        self.assertEqual(233168, Problem1().solve())

    def testProblem2(self):
        self.assertEqual(4613732, Problem2().solve())

    def testProblem3(self):
        self.assertEqual(6857, Problem3().solve())

    def testProblem4(self):
        self.assertEqual(906609, Problem4().solve())

    def testProblem5(self):
        self.assertEqual(232792560, Problem5().solve())


if __name__ == "__main__":
    unittest.main()
