"""
19.Remove Nth Node From End of List [Medium]
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         count = 0
#         curr = head
#         while curr:
#             curr = curr.next
#             count += 1
        
#         pre_index = count - n - 1
#         curr = head
        
#         for _ in range(pre_index):
#             curr = curr.next
            
#         curr.next = curr.next.next
        
#         return head
        
        dummy = ListNode(0, head)
        
        left = dummy  
        right = head
        
        for _ in range(n):
            right = right.next
            
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return dummy.next