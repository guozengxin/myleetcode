#!/usr/bin/env python
# https://oj.leetcode.com/problems/unique-paths/


class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        N = m - 1 + n - 1
        K = min(m, n) - 1
        res = 1
        for i in xrange(K):
            res = res * (N - i) / (i + 1)
        return res

if __name__ == '__main__':
    print Solution().uniquePaths(10, 5)
    print Solution().uniquePaths(3, 2)
    print Solution().uniquePaths(2, 2)
