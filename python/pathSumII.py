#!/usr/bin/env python
# https://oj.leetcode.com/problems/path-sum-ii/


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        result = []
        queue = [[root, 0, sum]]
        while len(queue) > 0:
            curr, flag, cursum = queue[-1]
            if curr is None:
                queue.pop()
                continue
            if queue[-1][1] == 0:
                queue[-1][1] = 1
                if curr.left is not None:
                    queue.append([curr.left, 0, cursum - curr.val])
                    continue
            if queue[-1][1] == 1:
                queue[-1][1] = 2
                if curr.right is not None:
                    queue.append([curr.right, 0, cursum - curr.val])
                    continue
            if curr.right is None and curr.left is None and curr.val == cursum:
                result.append([item[0].val for item in queue])
            queue.pop()

        return result

if __name__ == '__main__':
    a = TreeNode(-2)
    a.right = TreeNode(-3)
    print Solution().pathSum(a, -5)
