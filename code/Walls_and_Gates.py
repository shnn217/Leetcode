"""
286.Walls and Gates [Medium]
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2**31 - 1
        q = collections.deque()
        GATE = 0
        row = len(rooms)
        col = len(rooms[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == GATE:
                    q.append((i,j))
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if new_r < 0 or new_c < 0 or new_r >= row or new_c >= col or rooms[new_r][new_c] != EMPTY:
                    continue
                
                rooms[new_r][new_c] = rooms[r][c] + 1
                q.append((new_r, new_c))
            