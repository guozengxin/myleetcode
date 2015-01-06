#!/usr/bin/env python
# https://oj.leetcode.com/problems/word-break/


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        lens = len(s)
        dp = [False for i in range(lens + 1)]
        dp[0] = True
        for i in range(1, lens + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
        return dp[lens]

if __name__ == '__main__':
    s = 'leetcode'
    dict = {'leet': 1, 'code': 1}
    print Solution().wordBreak(s, dict)
    print Solution().wordBreak('leetc', dict)
