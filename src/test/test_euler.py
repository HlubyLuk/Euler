# coding: UTF-8

'''
Created on Nov 3, 2018

@author: HlubyLuk
'''
import unittest
from euler.euler import *


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
        factors = {2: 2, 3: 1, 5: 1}
        self.assertDictEqual(factors, MockProblem().prime_factors(60))

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
        sieve = [True, True, False, False, True, False, True, False]
        self.assertListEqual(sieve, MockProblem().eratosthenes_sief(7))

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

    def test_problem19(self):
        self.assertEqual(171, Problem19().solve())

    def test_problem20(self):
        self.assertEqual(648, Problem20().solve())

    def test_problem21(self):
        self.assertEqual(31626, Problem21().solve())

    def test_divisors(self):
        self.assertListEqual([1, 2, 5], MockProblem().divisors(10))

    def test_amicable_number_ok(self):
        self.assertTrue(MockProblem().is_amicable_number(220))

    def test_amicable_number_ko(self):
        self.assertFalse(MockProblem().is_amicable_number(110))

    def test_problem22(self):
        self.assertEqual(871198282, Problem22().solve())

    def test_problem23(self):
        self.assertEqual(4179871, Problem23().solve())

    def test_is_abundant_ok(self):
        self.assertTrue(MockProblem().is_abundant(12))

    def test_is_abundant_ko(self):
        self.assertFalse(MockProblem().is_abundant(17))

    def test_problem24(self):
        self.assertEqual(2783915460, Problem24().solve())

    def test_next_lexigonal_permutation_ok(self):
        seq = [1, 2, 3, 4]
        MockProblem.Permutation().next_lexigonal_permutation(seq)
        self.assertListEqual([1, 2, 4, 3], seq)

    def test_next_lexigonal_permutation_true(self):
        perm = MockProblem.Permutation()
        self.assertTrue(perm.next_lexigonal_permutation([1, 2, 3, 4]))

    def test_next_lexigonal_permutation_false(self):
        perm = MockProblem.Permutation()
        self.assertFalse(perm.next_lexigonal_permutation([4, 3, 2, 1]))

    def test_problem25(self):
        self.assertEqual(4782, Problem25().solve())

    def test_fibonacci_sequence_ok(self):
        self.assertEqual((2, 3), MockProblem().next_fibonacci(1, 2))

    def test_fibonacci_sequence_ko(self):
        self.assertNotEqual((3, 5), MockProblem().next_fibonacci(1, 2))

    def test_problem26(self):
        self.assertEqual(983, Problem26().solve())

    def test_problem27(self):
        self.assertEqual(-59231, Problem27().solve())

    def test_problem28(self):
        self.assertEqual(669171001, Problem28().solve())

    def test_problem29(self):
        self.assertEqual(9183, Problem29().solve())

    def test_problem30(self):
        self.assertEqual(443839, Problem30().solve())

    def test_problem31(self):
        self.assertEqual(73682, Problem31().solve())

    def test_coins_solver_ok(self):
        ccs = MockProblem.CoinsChangeSolver([1, 2, 3], 4)
        self.assertEqual(4, ccs.solve())

    def test_problem32(self):
        self.assertEqual(45228, Problem32().solve())

    def test_problem33(self):
        self.assertEqual(100, Problem33().solve())

    def test_gcd_5(self):
        self.assertEqual(5, MockProblem().gcd(15, 10))

    def test_gcd_6(self):
        self.assertEqual(6, MockProblem().gcd(30, 12))

    def test_problem34(self):
        self.assertEqual(40730, Problem34().solve())

    def test_factorial_lambda_ok(self):
        self.assertEqual(24, MockProblem().factorial_lambda(4))

    def test_factorial_lambda_ko(self):
        self.assertNotEqual(121, MockProblem().factorial_lambda(5))

    def test_problem35(self):
        self.assertEqual(55, Problem35().solve())

    def test_problem36(self):
        self.assertEqual(872187, Problem36().solve())

    def test_problem37(self):
        self.assertEqual(748317, Problem37().solve())

    def test_problem38(self):
        self.assertEqual(932718654, Problem38().solve())

    def test_problem39(self):
        self.assertEqual(840, Problem39().solve())

    def test_problem40(self):
        self.assertEqual(210, Problem40().solve())

    def test_problem41(self):
        self.assertEqual(7652413, Problem41().solve())

    def test_problem42(self):
        self.assertEqual(162, Problem42().solve())

    def test_problem43(self):
        self.assertEqual(16695334890, Problem43().solve())

    def test_problem44(self):
        self.assertEqual(5482660, Problem44().solve())

    def test_problem45(self):
        self.assertEqual(1533776805 , Problem45().solve())

    def test_problem46(self):
        self.assertEqual(5777, Problem46().solve())

    def test_problem47(self):
        self.assertEqual(134043, Problem47().solve())

    def test_problem48(self):
        self.assertEqual(9110846700 , Problem48().solve())

    def test_problem49(self):
        self.assertEqual(296962999629, Problem49().solve())

    def test_problem50(self):
        self.assertEqual(997651, Problem50().solve())


class MockProblem(Problem):

    def solve(self):
        return Problem.solve(self)


if __name__ == "__main__":
    unittest.main()
