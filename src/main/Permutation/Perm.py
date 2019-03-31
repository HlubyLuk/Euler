'''
Created on Mar 31, 2019

@author: hlubyluk
'''


class Permutation(object):

    def __init__(self):
        pass

    def _reverse(self, value, start, end):
        while start < end:
            self._swap(value, start, end)

            start += 1
            end -= 1

    def _swap(self, value, k, l):
        tmp = value[k]
        value[k] = value[l]
        value[l] = tmp

    def next_lexigonal_permutation(self, current):
        pivot_k = len(current) - 2
        while pivot_k >= 0 and current[pivot_k] >= current[pivot_k + 1]:
            pivot_k -= 1

        if pivot_k == -1:
            return False

        pivot_l = len(current) - 1
        while current[pivot_k] >= current[pivot_l]:
            pivot_l -= 1

        self._swap(current, pivot_k, pivot_l)
        self._reverse(current, pivot_k + 1, len(current) - 1)

        return True
