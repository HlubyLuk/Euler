#!/usr/bin/env python
# coding=utf-8
from problem.Problem import Problem

EDGE = 20


class Problem15(Problem):
    """
    Lattice paths
    Problem 15

    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
    there are exactly 2 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
    """

    def solve(self):
        return self.binomical_coeficient(EDGE + EDGE, EDGE)
