# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        chars = {}
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        for c in t:
            if c not in chars:
                return False
            else:
                chars[c] -= 1
                if chars[c] < 0:
                    return False
        return True

s = "anagram"
t = "nagaram"
print Solution().isAnagram(s, t)
s = "rat"
t = "car"
print Solution().isAnagram(s, t)
