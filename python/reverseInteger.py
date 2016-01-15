# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        if x < 0:
            ret = -int(str(-x)[::-1])
        else:
            ret = int(str(x)[::-1])
        if ret > 2 ** 31 - 1 or ret < -(2 ** 31):
            ret = 0
        return ret
