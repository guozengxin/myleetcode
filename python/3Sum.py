# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in xrange(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                while (r < len(nums) - 1) and r > i and nums[r] == nums[r+1]:
                    r -= 1
                while l > i + 1 and l < len(nums) and nums[l] == nums[l-1]:
                    l += 1
        return res

nums = [0,0,0]
solution = Solution()
print solution.threeSum(nums)
