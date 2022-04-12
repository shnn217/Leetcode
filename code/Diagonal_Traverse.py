"""
498.Diagonal Traverse [Medium]
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        ans = []
        
    
        for i in range(m + n - 1):
            if i % 2 == 0:
                row, col = i if i < m else m - 1, 0 if i < m else i - m + 1
                while 0 <= row < m and 0 <= col < n:
                    ans.append(mat[row][col])
                    row -= 1
                    col += 1
            else:
                row, col = 0 if i < n else i - n + 1, i if i < n else n - 1
                while 0 <= row < m and 0 <= col < n:
                    ans.append(mat[row][col])
                    row += 1
                    col -= 1
            
        return ans
