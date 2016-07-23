#!/usr/bin/python
# coding=utf-8

"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

find the largest palindrome made from the product of two 3-digit numbers.
"""

ret = []
for i in range(99, 999):
    for j in range(99, 999):
        a = i * j
        if str(a) == str(a)[::-1]:
            ret.append(a)
print max(ret)
print min(ret)

