#!/usr/bin/env python
# https://oj.leetcode.com/problems/excel-sheet-column-number/


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        s = s[::-1]
        result = 0
        for i in range(len(s)):
            n = ord(s[i]) - ord('A') + 1
            result += n * (26 ** i)
        return result

if __name__ == '__main__':
    print Solution().titleToNumber('A')
    print Solution().titleToNumber('B')
    print Solution().titleToNumber('Z')
    print Solution().titleToNumber('ZZ')
    print Solution().titleToNumber('AA')
