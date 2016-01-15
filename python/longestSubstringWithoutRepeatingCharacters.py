#!/usr/bin/env python
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        last_pos = {}
        result = [1] * len(s)
        for i in xrange(len(s)):
            if i > 0:
                last = last_pos.get(s[i], -1)
                if last < i - result[i-1]:
                    result[i] = result[i-1] + 1
                else:
                    result[i] = i - last
            last_pos[s[i]] = i
        return max(result)

strs = [
    'abcabcbb',
    'bbbbb'
]
so = Solution()
for s in strs:
    print s, so.lengthOfLongestSubstring(s)
