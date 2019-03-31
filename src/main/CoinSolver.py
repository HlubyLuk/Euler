'''
Created on Mar 31, 2019

@author: hlubyluk
'''


class CoinSolver(object):
    '''
    Help solve how many combinations should change target value.
    :see
    https://hackernoon.com/the-coin-change-problem-explained-ddd035a8f22f
    '''

    def __init__(self, values, target):
        '''
        Constructor.
        :values `list` of coins.
        :target price.
        '''
        self.v = values
        self.c = target

    def solve(self):
        '''
        Solve count of combinations.
        :return count of combinations target value.
        '''
        table = [[0 for _ in range(0, len(self.v))]
                 for _ in range(0, self.c + 1)]

        for i in range(0, len(self.v)):
            table[0][i] = 1

        for i in range(1, self.c + 1):
            for j in range(len(self.v)):
                x = table[i - self.v[j]][j] if i - self.v[j] >= 0 else 0
                y = table[i][j - 1]if j >= 1 else 0

                table[i][j] = x + y

        return table[-1][-1]
