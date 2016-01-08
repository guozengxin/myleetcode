# https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return (n & (n-1)) == 0

s = Solution()
for i in xrange(100):
    print i, s.isPowerOfTwo(i)