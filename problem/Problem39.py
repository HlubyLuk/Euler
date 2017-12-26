# -*- coding=utf-8 -*-
from problem.Problem import Problem


class Problem39(Problem):
    """
    Integer right triangles
    Problem 39
    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
    """


    def solve(self):
        return max([(p, len([(a, b) for a in range(1, p // 3) for b in
            range(a + 1, p // 2) if a * a + b * b == (p - a - b) * (p - a - b)]))
            for p in range(1, 1001)], key = lambda x: x[1])[0]
        pass
    pass
