#!/usr/bin/env python
# https://oj.leetcode.com/problems/candy/


class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        lenr = len(ratings)
        cadies = [1] * lenr
        for i in range(1, lenr):
            if ratings[i] > ratings[i - 1]:
                cadies[i] = cadies[i - 1] + 1
        for i in range(lenr - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and cadies[i + 1] >= cadies[i]:
                cadies[i] = cadies[i + 1] + 1
        return sum(cadies)
