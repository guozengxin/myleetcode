#!/usr/bin/env python
# https://oj.leetcode.com/problems/single-number-ii/


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d = {}
        for i in A:
            if i not in d:
                d[i] = 0
            d[i] += 1
        for i in d:
            if d[i] != 3:
                return i

if __name__ == '__main__':
    print Solution().singleNumber([1, 2, 3, 2, 3, 2, 3])
