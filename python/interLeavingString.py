#!/usr/bin/env python
# https://oj.leetcode.com/problems/interleaving-string/


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False
        isMatch = [[False for i in range(len2 + 1)] for j in range(len1 + 1)]
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 and j == 0:
                    isMatch[i][j] = True
                    continue
                if i > 0 and j == 0:
                    isMatch[i][j] = isMatch[i - 1][j] and s1[i - 1] == s3[i - 1]
                    continue
                if j > 0 and i == 0:
                    isMatch[i][j] = isMatch[i][j - 1] and s2[j - 1] == s3[j - 1]
                    continue
                isMatch[i][j] = (isMatch[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (isMatch[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return isMatch[len1][len2]


if __name__ == '__main__':
    print Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'), True
    print Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc'), False
    print Solution().isInterleave('a', '', 'a'), True
    print Solution().isInterleave('', '', 'a'), False
