# https://leetcode.com/problems/integer-to-roman/

class Solution(object):

    chars = [('I', 'V'), ('X', 'L'), ('C', 'D'), ('M')]

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = map(int, list(str(num)))
        index = 0
        result = ''
        for n in reversed(nums):
            if n <= 3:
                result = self.chars[index][0] * n + result
            elif n == 4:
                result = self.chars[index][0] + self.chars[index][1] + result
            elif n >= 5 and n <= 8:
                result = self.chars[index][1] + self.chars[index][0] * (n - 5) + result
            elif n == 9:
                result = self.chars[index][0] + self.chars[index+1][0] + result
            index += 1
        return result

nums = [
    1,
    2,
    8,
    13,
    19,
    49,
    50,
    69,
    440,
    87,
    2034,
]

s = Solution()
for n in nums:
    print n, s.intToRoman(n)
