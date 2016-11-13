from problem.Problem import Problem

class Problem5(Problem):
    """
    Smallest multiple
    Problem 5

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """

    def solve(self):
        arr = range(1, 21)
        tmp = 1
        while True:
            check = True
            for j in arr:
                check = tmp % j == 0
                if not check:
                    break
            if check:
                break
            tmp += 1
        return tmp
