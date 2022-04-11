"""
54.Spiral Matrix [Medium]
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        counter = 1
        ans = [ ]
        number = 0
        if m <= n:
            number = 2*m - 1
        else:
            number = 2*n 
        
        r, c = 0, 0
        h, v = n, m
        if m == 1:
            return matrix[0]
        elif n == 1:
            for i in range(m):
                ans.append(matrix[i][0])
            return ans
        
        for i in range(number):
            if i % 4 == 0:
                while c < n + 1 - counter:
                    ans.append(matrix[r][c])
                    c += 1
                    if c == n + 1 - counter:
                        c -= 1
                        break
                r += 1
            if i % 4 == 1:
                while r < m + 1 - counter:
                    ans.append(matrix[r][c])
                    r += 1
                    if r == m + 1 - counter:
                        r -= 1
                        break
                c -= 1
            if i % 4 == 2:
                while c > -2 + counter:
                    ans.append(matrix[r][c])
                    c -= 1
                    if c == -2 + counter:
                        c += 1
                        break
                r -= 1
            if i % 4 == 3:
                while r > -1 + counter :
                    ans.append(matrix[r][c])
                    r -= 1
                    if r ==  -1 + counter:
                        r += 1
                        break
                c += 1
                counter += 1
            
            
        return ans
                    