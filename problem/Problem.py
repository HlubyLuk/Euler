#!/usr/bin/python
# coding=utf-8
"""
https://projecteuler.net/about
"""
import math
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
        raise NotImplementedError('subclasses must override foo()!')

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

        for i in range(1, int(math.sqrt(number))):
            if number % i == 0:
                ret += 1

        return ret * 2
