#!/usr/bin/python
# coding=utf-8
"""
https://projecteuler.net/about
"""
from abc import abstractmethod


class Problem(object):
    """
    Abstract parent class
    Must implement method solve
    """

    @abstractmethod
    def solve(self):
        """
        Implementation of solution of problem.
        print result.
        """
        raise NotImplementedError('subclasses must override solve() method!')

    @staticmethod
    def is_prime(number):
        """
        Try prime factorization
        :param number: int to resolve
        :return: if is prime number return True, otherwise False
        """
        if number == 2:
            return True
        if number % 2 == 0 or number < 2:
            return False
        for i in range(3, int(number ** .5) + 1, 2):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def triangle_number(number):
        """
        This sequence is generated from a pattern of dots which form a triangle.
        By adding another row of dots and counting all the dots we can find the next number of the sequence.
        :param number: edge of triangle
        :return: count of triangles.
        """
        return (number * (number + 1)) / 2

    @staticmethod
    def count_dividers(number):
        """
        Compute count of dividers.
        :param number: to factorization.
        :return: count of dividers.
        """
        ret = 0
        for i in range(1, int(number ** .5)):
            if number % i == 0:
                ret += 1
        return ret * 2

    def binomical_coeficient(self, n, k):
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))

    def factorial(self, n):
        if n == 1:
            ret = 1
        else:
            ret = n * self.factorial(n - 1)
        return ret

    def is_amicable(self, a):
        b = self.sum_of_dividers(a)
        return a == self.sum_of_dividers(b) and a != b

    def sum_of_dividers(self, a):
        dividers = 0
        for i in range(1, a):
            if a % i == 0:
                dividers+=i
        return dividers
