'''
This is a problem on leetcode.com
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists of non-negative integers.
The digits are stored in reverse order and each of their nodes
contain a single digit.

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def _addHelper(self, l1, l2, head, curr, carry_over):
        if not l1 and not l2:
            if carry_over == 1:
                curr.next = ListNode(1)
            return head

        if not l1:
            val = l2.val + carry_over
            l2 = l2.next
        elif not l2:
            val = l1.val + carry_over
            l1 = l1.next
        else:
            val = l1.val + l2.val + carry_over
            l2 = l2.next
            l1 = l1.next

        next_node = ListNode(val % 10)

        if not head:
            head = next_node
            curr = head
        else:
            curr.next = next_node
            curr = next_node

        return self._addHelper(l1, l2, head, curr, val // 10)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self._addHelper(l1, l2, None, None, 0)
