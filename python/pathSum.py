#!/usr/bin/env python
# https://oj.leetcode.com/problems/path-sum/


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        l = sum - root.val
        return self.hasPathSum(root.left, l) or self.hasPathSum(root.right, l)

if __name__ == '__main__':
    a = TreeNode(2)
    a.left = None
    a.right = None
    b = TreeNode(1)
    b.left = a
    b.right = None
    print Solution().hasPathSum(b, 3)
