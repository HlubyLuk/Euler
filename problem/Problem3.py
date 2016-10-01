from problem.Problem import Problem


class Problem3(Problem):
    """
    Largest prime factor
    Problem 3

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    to_resolve = 600851475143

    def solve(self):
        i, tmp = 1, 0
        while self.to_resolve != 1:
            if self.to_resolve % i == 0:
                self.to_resolve /= i
                tmp = i
                i = 1
            i += 1
        return tmp
