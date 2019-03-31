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


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_problem1']
    unittest.main()
