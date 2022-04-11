"""
119.Pascal's Triangle || [Easy]
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ans = [[1],[1,1]]
        
        while rowIndex > 1:
            current = ans[-1]
            temp = []
            for i in range(len(current) - 1):
                temp.append(current[i]+current[i+1])
            ans.append([1]+temp+[1])
            rowIndex-=1
        
        return ans[-1]