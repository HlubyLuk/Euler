from problem.Problem import Problem

START_SEQUENCE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
STOP = 1000000
# START_SEQUENCE = [0, 1, 2]
# STOP = 6


class Problem24(Problem):
    """
    Lexicographic permutations
    Problem 24

    A permutation is an ordered arrangement of objects.
    For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
    If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
    The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """

    def solve(self):
        tmp = 1
        while tmp < STOP:
            self.nextLexicographicPermutations(START_SEQUENCE)
            tmp += 1

        return ''.join([str(i) for i in START_SEQUENCE])
