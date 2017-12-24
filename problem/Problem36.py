from problem.Problem import Problem


class Problem36(Problem):
    """
    Double-base palindromes

    Problem 36

    The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
    Find the sum of all numbers, less than one million, which are palindromic in
    base 10 and base 2. (Please note that the palindromic number, in either
    base, may not include leading zeros.)
    """


    def solve(self):
        return sum([x for x in range(1, 1000000) if
            self.is_palindrome_double(x)])


    def is_palindrome_double(self, a):
        return self.is_palindrome_10(a) and self.is_palindrome_2(a)
