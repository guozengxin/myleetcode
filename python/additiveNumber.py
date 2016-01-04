# https://leetcode.com/problems/additive-number/


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        for i in range(2, len(num) * 2 / 3 + 1):
            for j in range(1, i):
                if self.checkNumber(num, j, i):
                    return True
        return False

    def checkNumber(self, num, first, second):
        firstNum = int(num[:first])
        secondNum = int(num[first:second])
        if (num[0] == '0' and firstNum != 0) or (num[first] == '0' and secondNum != 0):
            return False
        while True:
            sumInt = firstNum + secondNum
            sumLen = len(str(sumInt))
            if num[second] == '0' and sumInt != 0:
                return False
            if (int(num[second:second + sumLen]) != sumInt):
                return False
            if (second + sumLen == len(num)):
                return True
            first = second
            second = second + sumLen
            firstNum = secondNum
            secondNum = sumInt
        return False


nums = ["199100199",
        "198019823962"
        ]
s = Solution()
for n in nums:
    print n, s.isAdditiveNumber(n)

