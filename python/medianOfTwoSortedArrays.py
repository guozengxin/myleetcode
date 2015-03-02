#!/usr/bin/env python
# https://oj.leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        aLen = len(A)
        bLen = len(B)
        oddNumber = False
        if (aLen + bLen) % 2 == 0:
            middleIdx = (aLen + bLen) / 2 - 1
            oddNumber = True
        else:
            middleIdx = (aLen + bLen) / 2
        aIdx, bIdx = 0, 0
        idx = 0
        medianSum = 0
        while aIdx < aLen and bIdx < bLen:
            if idx == middleIdx:
                if A[aIdx] < B[bIdx]:
                    medianSum += A[aIdx]
                    aIdx += 1
                else:
                    medianSum += B[bIdx]
                    bIdx += 1
                if oddNumber:
                    middleIdx += 1
                    oddNumber = False
                else:
                    idx += 1
                    break
            else:
                if A[aIdx] < B[bIdx]:
                    aIdx += 1
                else:
                    bIdx += 1
            idx += 1

        while idx <= middleIdx and aIdx < aLen:
            if idx == middleIdx:
                medianSum += A[aIdx]
                if oddNumber:
                    middleIdx += 1
                    oddNumber = False
                else:
                    idx += 1
                    break
            aIdx += 1
            idx += 1
        while idx <= middleIdx and bIdx < bLen:
            if idx == middleIdx:
                medianSum += B[bIdx]
                if oddNumber:
                    middleIdx += 1
                    oddNumber = False
                else:
                    idx += 1
                    break
            idx += 1
            bIdx += 1

        if (aLen + bLen) % 2 == 0:
            return medianSum / 2.0
        else:
            return medianSum

if __name__ == '__main__':
    A = []
    B = [1, 2]
    print Solution().findMedianSortedArrays(A, B)
