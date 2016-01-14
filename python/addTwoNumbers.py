# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1
        result = l1
        l1.val += l2.val
        while l1.next is not None and l2.next is not None:
            if l1.val > 9:
                l1.next.val += l1.val / 10
                l1.val = l1.val % 10
            l1.next.val += l2.next.val
            l1 = l1.next
            l2 = l2.next

        if l2.next is not None:
            l1.next = l2.next

        while l1.val > 9:
            l1.val %= 10
            if l1.next is None:
                l1.next = ListNode(1)
            else:
                l1.next.val += 1
                l1 = l1.next
        return result


l1 = ListNode(0)
l1.next = None

l2 = ListNode(7)
l2.next = ListNode(3)

s = Solution()
s.addTwoNumbers(l1, l2)