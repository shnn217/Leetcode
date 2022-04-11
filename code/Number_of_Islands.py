"""
200.Number of Islands [Medium]
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        m = len(grid)
        n = len(grid[0])
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    count += 1
    
        return count
    
    
    def valid_index(self, grid, r, c) -> bool:
        m = len(grid)
        n = len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True
    
    def bfs(self, grid, r, c):        
        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        q.append((r,c))
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        grid[r][c] = 0                                 
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if self.valid_index(grid, new_r, new_c) and grid[new_r][new_c] == "1":
                    q.append((new_r, new_c))
                    grid[new_r][new_c] = "0"
        
        
                    
        