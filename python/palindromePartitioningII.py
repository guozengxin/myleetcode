#!/usr/bin/env python
# https://oj.leetcode.com/problems/palindrome-partitioning-ii/


class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        slen = len(s)
        subPalindrome = [[False for i in range(slen)] for j in range(slen)]
        cuts = [0] * slen
        for i in range(0, slen):
            cuts[i] = slen - i - 1
        for i in range(slen - 1, -1, -1):
            for j in range(i, slen):
                if s[i] == s[j] and (j - i in (0, 1) or subPalindrome[i + 1][j - 1]):
                    if j == slen - 1:
                        cuts[i] = 0
                    else:
                        cuts[i] = min(cuts[i], 1 + cuts[j + 1])
                    subPalindrome[i][j] = True
        return cuts[0]

if __name__ == '__main__':
    import sys
    print Solution().minCut(sys.argv[1])
