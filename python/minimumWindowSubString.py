#!/usr/bin/env python
# https://oj.leetcode.com/problems/minimum-window-substring/


class Solution:
    # @return a string
    def minWindow(self, S, T):
        lens, lenT = len(S), len(T)
        tChars = {}
        for t in T:
            if t not in tChars:
                tChars[t] = 0
            tChars[t] += 1
        hasFound = {}
        foundCount = 0
        start, end = 0, 0
        isInT = [False] * lens
        minStart, minEnd = -1, lens
        while end < lens:
            c = S[end]
            if c in tChars:
                isInT[end] = True
                if c not in hasFound:
                    hasFound[c] = 0
                hasFound[c] += 1
                if hasFound[c] <= tChars[c]:
                    foundCount += 1
                if foundCount == lenT:
                    while True:
                        startC = S[start]
                        if not isInT[start]:
                            start += 1
                            continue
                        elif hasFound[startC] > tChars[startC]:
                            start += 1
                            hasFound[startC] -= 1
                            continue
                        break
                    if end - start < minEnd - minStart:
                        minEnd, minStart = end, start
            end += 1
        if minStart == -1:
            return ''
        else:
            return S[minStart:minEnd + 1]

if __name__ == '__main__':
    print Solution().minWindow('ADOBECODEBANC', 'ABC'), 'BANC'
    print Solution().minWindow('acbbaca', 'aba'), 'baca'
