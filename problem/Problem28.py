from problem.Problem import Problem


EDGE = 1001

class Problem28(Problem):
    """
    Number spiral diagonals
    Problem 28

    Starting with the number 1 and moving to the right in
    a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001
    spiral formed in the same way?
    """    

    def solve(self):
        edges = EDGE * EDGE
        matrix, index, shift = [0] * edges, 0, 2
        for i in range(0, edges):
            index += 1
            matrix[i] = index
        added = []
        for i, val in enumerate(matrix):
            if i > 0 and i % shift == 0:
                added.append(val)
                if len(added) % 4 == 0:
                    shift += 2
        added.append(matrix[0])
        return sum(added)
