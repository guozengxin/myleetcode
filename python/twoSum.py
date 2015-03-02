#!/usr/bin/env python
# https://oj.leetcode.com/problems/two-sum/


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        length = len(num)
        numbers = sorted(num)
        left = 0
        right = length - 1
        index = []
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                for i in range(length):
                    if num[i] == numbers[left]:
                        index.append(i + 1)
                    elif num[i] == numbers[right]:
                        index.append(i + 1)
                break
            elif s > target:
                right -= 1
            else:
                left += 1

        return tuple(index)

if __name__ == '__main__':
    fp = open('n.txt', 'r')
    line = fp.readline()
    arr = line.split(',')
    num = [int(a) for a in arr]
    num = [0, 4, 3, 0]
    target = 0
    print Solution().twoSum(num, target)
