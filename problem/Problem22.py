#!/usr/bin/ python
# coding=utf-8
import os
import posixpath

from problem.Problem import Problem


class Problem22(Problem):
    """
    Names scores
    Problem 22

    Using names.txt (in asset directory), a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order.
    Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN,
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """

    def solve(self):
        a = open(os.getcwd() + posixpath.sep + "asset" + posixpath.sep + "names.txt")
        str_from_file = str()
        for line in a.readlines():
            str_from_file = str_from_file.join(line)
        str_from_file = str_from_file.replace("\"", "")
        sorted_names = sorted(str_from_file.split(","))

        ret = 0
        for i, val in enumerate(sorted_names):
            tmp = i + 1
            name_score = 0
            for j, lav in enumerate(val):
                name_score += ord(lav) - ord("A") + 1
            ret += tmp * name_score
        return ret
