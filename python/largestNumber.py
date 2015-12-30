#!/usr/bin/env python
# https://leetcode.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strs = sorted(map(str, nums), self.compare)
        s = ''.join(strs).lstrip('0')
        return s or '0'

    def compare(self, a, b):
        if a + b > b + a:
            return -1
        else:
            return 1


nums = [3, 30, 34, 5, 9]
s = Solution()
print s.largestNumber(nums)
nums = [0, 0, 0]
print s.largestNumber(nums)
