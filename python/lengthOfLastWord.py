# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.strip().split(' ')
        if len(a) == 0:
            return 0
        return len(a[-1])

solu = Solution()
ss = [
    'Hello World',
    'a',
    'a ',
    ' a',
    'a a '
]
for s in ss:
    print '"' + s + '"', solu.lengthOfLastWord(s)