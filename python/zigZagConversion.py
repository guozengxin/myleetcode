# https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        if numRows == 1:
            return s
        zigSize = numRows * 2 - 2
        result = ''
        for i in xrange(numRows):
            if i == 0 or i == numRows - 1:
                for j in xrange(i, size, zigSize):
                    result += s[j]
            else:
                for j in xrange(i, size, zigSize):
                    result += s[j]
                    next = j + (numRows - i - 1) * 2
                    if next < size:
                        result += s[next]
        return result

string = 'PAYPALISHIRING'
s = Solution()
print s.convert(string, 3)
