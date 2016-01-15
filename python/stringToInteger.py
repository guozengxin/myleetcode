# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    MAX = 2 ** 31 - 1
    MIN = -(2**31)
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0

        flag = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            flag = -1
        for i in xrange(len(s)):
            if s[i] < '0' or s[i] > '9':
                s = s[:i]
                break
        if len(s) == 0:
            return 0
        i = int(s) * flag
        if i > self.MAX:
            i = self.MAX
        elif i < self.MIN:
            i = self.MIN
        return i



strs = [
    '123',
    '+123',
    '-234',
    '123412341234',
    '-123412341234',
    '123411aa',
    '+',
    '  -0012a42',
]

so = Solution()
for s in strs:
    print s, so.myAtoi(s)
