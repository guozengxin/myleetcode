# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        i, j = 0, 0
        while i < size:
            while i < size and nums[i] != 0:
                i += 1
            if i >= size:
                break
            j = i + 1
            while j < size and nums[j] == 0:
                j += 1
            if j >= size:
                break
            nums[j], nums[i] = nums[i], nums[j]

nums = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes(nums)
print nums
