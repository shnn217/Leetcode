"""
2.Add Two Numbers [Medium]
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
https://imgur.com/YsrAQv5
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        l1_head2 = l1
        temp = l1
        while l1 and l2:
            l1.val = l1.val + l2.val
            if l1.val >= 10:
                l1.val = l1.val - 10
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
            if not l1.next:
                temp = l1
            l1 = l1.next
            l2 = l2.nexts
        
        if not l1 and l2:
            temp.next = l2

        while l1_head2:
            if l1_head2.val >= 10:
                l1_head2.val -= 10
                if l1_head2.next:
                    l1_head2.next.val += 1
                else:
                    l1_head2.next = ListNode(1)
            l1_head2 = l1_head2.next
        
        return l1_head