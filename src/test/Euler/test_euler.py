'''
Created on Mar 31, 2019

@author: hlubyluk
'''
import unittest
from main.Euler import *


class Test(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(233168, problem1())

    def test_problem2(self):
        self.assertEqual(4613732, problem2())

    def test_problem3(self):
        self.assertEqual(6857, problem3())

    def test_problem4(self):
        self.assertEqual(906609, problem4())

    def test_palindrome_ok(self):
        self.assertTrue(is_palindrome("12344321"))

    def test_palindrome_ko(self):
        self.assertFalse(is_palindrome("123421"))

    def test_problem5(self):
        self.assertEqual(232792560, problem5())

    def test_prime_factorization_10(self):
        self.assertListEqual([(2, 1), (5, 1)], prime_factorization(10).items())

    def test_prime_factorization_12(self):
        self.assertListEqual([(2, 2), (3, 1)], prime_factorization(12).items())

    def test_mul_ok(self):
        self.assertEqual(12, mul(3, 4))

    def test_mul_ko(self):
        self.assertNotEqual(11, mul(3, 4))

    def test_pow_tupple_ok(self):
        self.assertEqual(27, pow_tupple((3, 3)))

    def test_pow_tupple_ko(self):
        self.assertNotEqual(5, pow_tupple((2, 2)))

    def test_problem6(self):
        self.assertEqual(25164150, problem6())

    def test_pow_fun_ok(self):
        self.assertEqual(27, pow_fun(3, 3))

    def test_pow_fun_ko(self):
        self.assertNotEqual(5, pow_fun(2, 2))

    def test_problem7(self):
        self.assertEqual(104743, problem7())

    def test_is_prime_13(self):
        self.assertTrue(is_prime(13))

    def test_is_prime_14(self):
        self.assertFalse(is_prime(14))

    def test_is_prime_15(self):
        self.assertFalse(is_prime(15))

    def test_problem8(self):
        self.assertEqual(23514624000, problem8())

    def test_problem9(self):
        self.assertEqual(31875000, problem9())

    def test_problem10(self):
        self.assertEqual(142913828922, problem10())

    def test_eratosthenes_sieve(self):
        result = [True] * 11
        result[2] = result[3] = result[5] = result[7] = False
        self.assertListEqual(result, eratosthenes_sieve(10))

    def test_problem11(self):
        self.assertEqual(70600674, problem11())

    def test_problem12(self):
        self.assertEqual(76576500, problem12())

    def test_factors_count_28(self):
        self.assertEqual(6, factors_count(28))

    def test_factors_count_21(self):
        self.assertEqual(4, factors_count(21))

    def test_problem13(self):
        self.assertEqual(5537376230, problem13())

    def test_problem14(self):
        self.assertEqual(837799, problem14())

    def test_problem15(self):
        self.assertEqual(137846528820, problem15())

    def test_binomial_coefficient(self):
        self.assertEqual(6, binomial_coefficient(4, 2))

    def test_factorial_3(self):
        self.assertEqual(6, factorial(3))

    def test_factorial_4(self):
        self.assertEqual(24, factorial(4))

    def test_factorial_5(self):
        self.assertEqual(120, factorial(5))

    def test_problem16(self):
        self.assertEqual(1366, problem16())

    def test_problem18(self):
        self.assertEqual(1074, problem18())

    def test_problem19(self):
        self.assertEqual(171, problem19())

    def test_problem20(self):
        self.assertEqual(648, problem20())

    def test_problem21(self):
        self.assertEqual(31626, problem21())

    def test_amicable_220(self):
        self.assertTrue(amicable(220))

    def test_amicable_222(self):
        self.assertFalse(amicable(222))

    def test_divisors(self):
        self.assertListEqual([1, 2, 5], divisors(10))

    def test_problem22(self):
        self.assertEqual(871198282, problem22())

    def test_problem23(self):
        self.assertEqual(4179871, problem23())

    def test_problem24(self):
        self.assertEqual(2783915460, problem24())

    def test_problem25(self):
        self.assertEqual(4782, problem25())

    def test_problem26(self):
        self.assertEqual(983, problem26())

    def test_problem27(self):
        self.assertEqual(-59231, problem27())

    def test_problem28(self):
        self.assertEqual(669171001, problem28())

    def test_problem29(self):
        self.assertEqual(9183, problem29())

    def test_problem30(self):
        self.assertEqual(443839, problem30())

    def test_problem31(self):
        self.assertEqual(73682, problem31())

    def test_problem32(self):
        self.assertEqual(45228, problem32())

    def test_problem33(self):
        self.assertEqual(100, problem33())

    def test_problem34(self):
        self.assertEqual(40730, problem34())

    def test_problem35(self):
        self.assertEqual(55, problem35())

    def test_problem36(self):
        self.assertEqual(872187, problem36())

    def test_problem37(self):
        self.assertEqual(748317, problem37())

    def test_problem38(self):
        self.assertEqual(932718654, problem38())


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_problem1']
    unittest.main()
