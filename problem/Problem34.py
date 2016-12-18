from problem.Problem import Problem
from math import factorial

class Problem34(Problem):

    def solve(self):
        return sum([x for x in range(3, 7 * factorial(9), 1) if x == sum(map(lambda y: factorial(int(y)), str(x)))])
