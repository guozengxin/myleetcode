# https://leetcode.com/problems/single-number-iii/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a, b = 0, 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num

        return [a, b]

nums = [1, 2, 1, 3, 2, 6]
s = Solution()
print s.singleNumber(nums)