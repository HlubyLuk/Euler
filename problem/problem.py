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
