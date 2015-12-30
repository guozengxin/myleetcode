#!/usr/bin/env python
# https://leetcode.com/problems/coin-change/

import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        s = [sys.maxint] * (amount + 1)
        s[0] = 0
        for c in coins:
            i = c
            while i <= amount:
                if s[i-c] != sys.maxint:
                    s[i] = min(s[i], s[i-c]+1)
                i += 1
        return s[amount] == sys.maxint and -1 or s[amount]

s = Solution()
coins = [186,419,83,408]
amount = 6249
print s.coinChange(coins, amount)
