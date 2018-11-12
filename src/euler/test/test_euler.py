'''
Created on Nov 3, 2018

@author: HlubyLuk
'''
import unittest
from euler.euler import Problem1, Problem2, Problem3, Problem4, Problem5, \
    Problem6, Problem7, Problem8, Problem, Problem9, Problem10, Problem11, \
    Problem12, Problem13, Problem14, Problem15, Problem16, Problem18


class Test(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(233168, Problem1().solve())

    def test_problem2(self):
        self.assertEqual(4613732, Problem2().solve())

    def test_problem3(self):
        self.assertEqual(6857, Problem3().solve())

    def test_problem4(self):
        self.assertEqual(906609, Problem4().solve())

    def test_problem5(self):
        self.assertEqual(232792560, Problem5().solve())

    def test_problem6(self):
        self.assertEqual(25164150, Problem6().solve())

    def test_problem7(self):
        self.assertEqual(104743, Problem7().solve())

    def test_problem8(self):
        self.assertEqual(23514624000, Problem8().solve())

    def testLcm(self):
        self.assertEqual(42, MockProblem().lcm([6, 21]))

    def test_primeFactors(self):
        self.assertEqual({2: 2, 3: 1, 5: 1}, MockProblem().prime_factors(60))

    def testIsPalindromic(self):
        self.assertTrue(MockProblem().is_palindromic(990099))

    def test_is_not_palidromic(self):
        self.assertFalse(MockProblem().is_palindromic(123456))

    def test_is_prime2(self):
        self.assertTrue(MockProblem().is_prime(2))

    def test_is_prime29(self):
        self.assertTrue(MockProblem().is_prime(29))

    def test_is_not_prime(self):
        self.assertFalse(MockProblem().is_prime(100))

    def test_problem9(self):
        self.assertEqual(31875000, Problem9().solve())

    def test_problem10(self):
        self.assertEqual(142913828922, Problem10().solve())

    def test_eratosthenes_sief(self):
        self.assertEqual([True, True, False, False, True, False, True, False],
                         MockProblem().eratosthenes_sief(7))

    def test_problem11(self):
        self.assertEqual(70600674, Problem11().solve())

    def test_problem12(self):
        self.assertEqual(76576500, Problem12().solve())

    def test_problem13(self):
        self.assertEqual(5537376230, Problem13().solve())

    def test_problem14(self):
        self.assertEqual(837799, Problem14().solve())

    def test_problem15(self):
        self.assertEqual(137846528820, Problem15().solve())

    def test_factorial_recursive(self):
        self.assertEqual(24, MockProblem().factorial(4))

    def test_combination_number(self):
        self.assertEqual(6, MockProblem().combination_number(2 + 2, 2))

    def test_problem16(self):
        self.assertEqual(1366, Problem16().solve())

    def test_problem18(self):
        self.assertEqual(1074, Problem18().solve())


class MockProblem(Problem):

    def solve(self):
        return Problem.solve(self)


if __name__ == "__main__":
    unittest.main()
