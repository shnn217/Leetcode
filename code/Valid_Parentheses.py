"""
20.Valid Parentheses [Easy]
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"}":"{", ")":"(", "]":"["}
        
        for char in s:
            if stack and (char in dic and stack[-1] == dic[char]):
                stack.pop()
            else:
                stack.append(char)
            
        return not stack
        