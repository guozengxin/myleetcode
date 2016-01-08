# https://leetcode.com/problems/rectangle-area/

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        if min(C, G) < max(A, E) or min(D, H) < max(B, F):
            overlap = 0
        return (C - A) * (D - B) + (G - E) * (H - F) - overlap


s = Solution()
print s.computeArea(-2, -2, 2, 2, -2, -2, 2, 2)
