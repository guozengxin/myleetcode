# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            lowH = height[i]
            highH = height[j]
            area = (j - i) * min(lowH, highH)
            maxArea = max(area, maxArea)
            if lowH < highH:
                while i < j and height[i] <= lowH:
                    i += 1
            else:
                while i < j and height[j] <= highH:
                    j -= 1
        return maxArea

height = [3, 2, 1, 3]
s = Solution()
print s.maxArea(height)
