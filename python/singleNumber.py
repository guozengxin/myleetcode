#!/usr/bin/env python
# https://oj.leetcode.com/problems/single-number/


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = A[0]
        for i in range(1, len(A)):
            ans = ans ^ A[i]
        return ans


if __name__ == '__main__':
    print Solution().singleNumber([1, 2, 3, 1, 2])
