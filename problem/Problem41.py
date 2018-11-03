'''
Created on Nov 3, 2018

@author: HlubyLuk
'''
from problem.Problem import Problem
import sys
import time

SEQUENCE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
LEN = len(SEQUENCE)


class Problem41(Problem):
    '''
    Pandigital prime
    Problem 41 
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.
    
    What is the largest n-digit pandigital prime that exists?
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    def seq_to_int(self, seq=[]):
        return int("".join(map(lambda x: str(x), seq)))
    
    def solve(self):
        ret = set()
        for limit in xrange(LEN, 0, -1):
            seq = SEQUENCE[0:limit]
            while self.next_permutation(seq):
                prime = self.seq_to_int(seq)
                if self.is_prime(prime):
                    ret.add(prime)
        return (sorted(ret).pop())
