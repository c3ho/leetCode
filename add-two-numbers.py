'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # This idiot question actually doesn't have a head function to get you back to the head, so we need need a dummy placeholder to go back to first node
        dummy = res = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            # calculate remainder for the value of the node
            res.next = ListNode(carry % 10)
            res = res.next
            # calculate the value to be brought to following node
            carry = carry // 10
        # Return dummy.next because we want the first node
        return dummy.next
