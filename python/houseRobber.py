# https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        a = 0
        b = 0
        for i in xrange(len(nums)):
            if i % 2 == 0:
                a += nums[i]
                a = max(a, b)
            else:
                b += nums[i]
                b = max(a, b)
        return max(a, b)