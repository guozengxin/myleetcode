# https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N = 1 << len(nums)
        res = []
        for i in xrange(N):
            res.append([])
        for i in xrange(N):
            for j in xrange(len(nums)):
                temp = 1 << j
                if i & temp:
                    res[i].append(nums[j])
        return res

s = Solution()
numsList = [
    [1, 2, 3],
    [3, 8, 7]
]

for nums in numsList:
    print s.subsets(nums)
