from problem.Problem import Problem

class Problem33(Problem):
    """
    Digit cancelling fractions
    Problem 33

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s. We shall consider
    fractions like, 30/50 = 3/5, to be trivial examples. There are exactly
    four non-trivial examples of this type of fraction, less than one in value,
    and containing two digits in the numerator and denominator. If the product
    of these four fractions is given in its lowest common terms, find the value
    of the denominator.
    """

    def solve(self):
        den_product, nom_product = 1, 1
        for i in range(1, 11, 1):
            for den in range(1, i, 1):
                for nom in range(1, den, 1):
                    if ((nom * 10 + i) * den == nom * (i * 10 + den)):
                        den_product *= den
                        nom_product *= nom
        return den_product / self.gcd(nom_product, den_product)
