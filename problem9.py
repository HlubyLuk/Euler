#!/usr/bin/python
# coding=utf-8
"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
total = 1000

if __name__ == "__main__":
    for a in range(1, total):
        for b in range(1, total):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print a * b * c
