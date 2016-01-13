# https://leetcode.com/problems/perfect-squares/

import sys
import math


class Solution(object):
    cache = [0] * 10001

    for i in range(1, 101):
        cache[i ** 2] = 1

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(2, n + 1):
            tmp = 10000
            if self.cache[i] != 0:
                continue
            for j in range(1, int(i ** 0.5) + 1):
                idx = i - j ** 2
                # print idx, "i", r[idx]
                tmp = tmp if tmp < self.cache[idx] else self.cache[idx]
            self.cache[i] = tmp + 1

        return self.cache[n]


s = Solution()
print s.numSquares(4128)
