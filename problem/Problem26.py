from problem.Problem import Problem

START = 2
STOP = 1000 + 1
STEP = 1


class ReciprocalSolver():
    """
    """
    
    precision = 1000

    def __init__(self, numerator = 1, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
        self.rests = set()
        self.numbers = ""
        self.x = 0

    def solve(self):
        count = 0
        self.x = self.numerator / self.denominator 
        rest = self.numerator % self.denominator
        while count < self.precision and rest > 0 and rest not in self.rests:
            self.rests.add(rest)
            rest *= 10
            self.numbers += str(rest / self.denominator)
            rest %= self.denominator
            count += 1
        return self


class Problem26(Problem):
    """
    Reciprocal cycles
    Problem 26

    A unit fraction contains 1 in the numerator.
    The decimal representation of the unit fractions with denominators 2 to 10 are given:

        1/2	= 	0.5
        1/3	= 	0.(3)
        1/4	= 	0.25
        1/5	= 	0.2
        1/6	= 	0.1(6)
        1/7	= 	0.(142857)
        1/8	= 	0.125
        1/9	= 	0.(1)
        1/10	= 	0.1 

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
    It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains
    the longest recurring cycle in its decimal fraction part.
    """    

    def solve(self):
        biggest = ReciprocalSolver()
        for i in range(START, STOP, STEP):
            tmp = ReciprocalSolver(1, i).solve()
            if len(biggest.numbers) < len(tmp.numbers):
                biggest = tmp
        return biggest.denominator
