'''
Created on Nov 3, 2018

@author: HlubyLuk
'''
import unittest
from euler.euler import Problem1, Problem2, Problem3, Problem4, Problem5,\
    Problem6, Problem7, Problem8, Problem


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

    def testProblem6(self):
        self.assertEqual(25164150, Problem6().solve())

    def testProblem7(self):
        self.assertEqual(104743, Problem7().solve())

    def testProblem8(self):
        self.assertEqual(23514624000, Problem8().solve())

    def testLcm(self):
        self.assertEqual(42, MockProblem().lcm([6, 21]))

    def testPrimeFactors(self):
        self.assertEqual({2: 2, 3: 1, 5: 1}, MockProblem().prime_factors(60))

    def testIsPalindromic(self):
        self.assertTrue(MockProblem().is_palindromic(990099))

    def testIsNotPalidromic(self):
        self.assertFalse(MockProblem().is_palindromic(123456))

    def testIsPrime2(self):
        self.assertTrue(MockProblem().is_prime(2))

    def testIsPrime29(self):
        self.assertTrue(MockProblem().is_prime(29))

    def testIsNotPrime(self):
        self.assertFalse(MockProblem().is_prime(100))


class MockProblem(Problem):

    def solve(self):
        return Problem.solve(self)


if __name__ == "__main__":
    unittest.main()
