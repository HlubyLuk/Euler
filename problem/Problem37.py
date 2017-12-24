from Problem import Problem


class Problem37(Problem):
    """
    Truncatable primes Problem 37 The number 3797 has an interesting property.
    Being prime itself, it is possible to continuously remove digits from left to
    right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
    work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to
    right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """
    def solve(self):
        return (sum([x for x in range(10, 748317) if self.trucatable(x)]))
        pass


    def trucatable(self, a):
        return self.is_prime(a) and self.prime_l_r(a) and self.prime_r_l(a)
        pass


    def prime_l_r(self, a):
        for x in range(1, len(str(a))):
            if not self.is_prime(int(str(a)[x::1])):
                return False
        return True
        pass


    def prime_r_l(self, a):
        for x in range(1, len(str(a))):
            if not self.is_prime(int(str(a)[:x:1])):
                return False
        return True
        pass
    pass
