# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        for i in xrange(len(s) / 2):
            if s[i] != s[-1-i]:
                return False
        return True

nums = [
    2,
    22,
    23,
    234,
    232,
    2332,
]

s = Solution()
for n in nums:
    print n, s.isPalindrome(n)
