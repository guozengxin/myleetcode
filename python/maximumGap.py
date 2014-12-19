#!/usr/bin/env python
# https://oj.leetcode.com/problems/maximum-gap/

import math


class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        size = len(num)
        if size < 2:
            return 0
        minValue = min(num)
        maxValue = max(num)
        minGap = int(math.ceil((maxValue - minValue) / float(size - 1)))
        bucketNum = (maxValue - minValue) / minGap + 1
        buckets = [None] * bucketNum
        for n in num:
            loc = int((n - minValue) / minGap)
            if buckets[loc] is None:
                buckets[loc] = [n, n]
            else:
                buckets[loc][0] = min(buckets[loc][0], n)
                buckets[loc][1] = max(buckets[loc][1], n)
        maxGap = 0
        for i in range(bucketNum):
            if buckets[i] is None:
                continue
            j = i + 1
            while j < bucketNum and buckets[j] is None:
                j += 1
            if j < bucketNum:
                maxGap = max(maxGap, buckets[j][0] - buckets[i][1])
            i = j
        return maxGap

if __name__ == '__main__':
    num = [3, 6, 9, 1]
    print Solution().maximumGap(num)
