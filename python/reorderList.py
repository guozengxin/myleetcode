#!/usr/bin/env python
# https://oj.leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        allNode = []
        h = head
        while h is not None:
            allNode.append(h)
            h = h.next
        lenAll = len(allNode)
        for i in range(len(allNode) / 2):
            allNode[i].next = allNode[lenAll - i - 1]
            allNode[lenAll - i - 1].next = allNode[i + 1]
        if lenAll % 2 == 1:
            allNode[lenAll / 2 + 1].next = allNode[lenAll / 2]
            allNode[lenAll / 2].next = None
        else:
            allNode[lenAll / 2].next = None


def p(head):
    while head is not None:
        print head.val, ' ',
        head = head.next
    print

if __name__ == '__main__':
    s1 = ListNode('s1')
    s2 = ListNode('s2')
    s3 = ListNode('s3')
    s4 = ListNode('s4')
    s5 = ListNode('s5')
    s6 = ListNode('s6')
    s1.next = s2
    s2.next = s3
    s3.next = s4
    s4.next = s5
    s5.next = s6
    s6.next = None
    Solution().reorderList(s1)
    p(s1)
