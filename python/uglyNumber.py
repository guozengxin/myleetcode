# https://leetcode.com/problems/ugly-number/

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True

        while num % 2 == 0:
            num = num / 2

        while num % 5 == 0:
            num = num / 5

        while num % 3 == 0:
            num = num / 3

        return num == 1

s = Solution()
for i in xrange(30):
    print i, s.isUgly(i)