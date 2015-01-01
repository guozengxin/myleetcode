#!/usr/bin/env python
# https://oj.leetcode.com/problems/excel-sheet-column-title/


class Solution:
    # @return a string
    def convertToTitle(self, num):
        s = ''
        while num > 0:
            r = num % 26
            num = num / 26
            if r == 0:
                s = 'Z' + s
                num -= 1
            else:
                s = chr((ord('A') + r - 1)) + s
        return s

if __name__ == '__main__':
    print Solution().convertToTitle(2)
    print Solution().convertToTitle(26)
    print Solution().convertToTitle(27)
