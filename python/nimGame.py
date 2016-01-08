# https://leetcode.com/problems/nim-game/

class Solution(object):


    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not n % 4 == 0

s = Solution()
for i in xrange(100):
    print i, s.canWinNim(i)