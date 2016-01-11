# https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for n in nums:
            sum += n
        l = len(nums)
        return l * (l + 1) / 2 - sum

nums = [0, 1, 3]
print Solution().missingNumber(nums)
nums = [1, 0]
print Solution().missingNumber(nums)