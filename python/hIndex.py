# https://leetcode.com/problems/h-index/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        h = len(citations)
        for c in citations:
            if c < h:
                h -= 1
            else:
                break
        return h

citations = [3, 0, 6, 1, 5]
print Solution().hIndex(citations)