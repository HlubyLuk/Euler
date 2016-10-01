from datetime import date
from problem.Problem import Problem
from dateutils import relativedelta


class Problem19(Problem):
    """
    Counting Sundays
    Problem 19

    You are given the following information, but you may prefer to do some research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """

    def solve(self):
        start, ret = date(1901, 1, 1), 0
        while start < date(2001, 1, 1):
            if start.weekday() == 6:
                ret += 1
            start = start + relativedelta(months=1)
        return ret
