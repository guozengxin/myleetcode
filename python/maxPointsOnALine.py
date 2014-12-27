#!/usr/bin/env python
# https://oj.leetcode.com/problems/max-points-on-a-line/
# Definition for a point


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        lines = {}
        maxNum = 0
        maxfloat = 1.7976931348623157e+308
        for p1 in points:
            lines = {}
            lines[2.2250738585072014e-308] = 0
            dup = 1
            for p2 in points:
                if p1 is p2:
                    continue
                if p1.x == p2.x and p1.y == p2.y:
                    dup += 1
                    continue
                if p1.x == p2.x:
                    if maxfloat not in lines:
                        lines[maxfloat] = 0
                    lines[maxfloat] += 1
                else:
                    k = float(p2.y - p1.y) / float(p2.x - p1.x)
                    if k not in lines:
                        lines[k] = 0
                    lines[k] += 1
            for key in lines:
                if lines[key] + dup > maxNum:
                    maxNum = lines[key] + dup
        return maxNum

if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(4, 3)
    p3 = Point(1, 4)
    p4 = Point(7, 5)

    l = [p1, p2, p3, p4]
    print Solution().maxPoints(l)
