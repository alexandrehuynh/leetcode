"""
Leetcode 200. Number of Islands: https://leetcode.com/problems/number-of-islands/description/

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
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

# DFS
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            # Base case: out of bounds or already visited
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                return
            
            grid[x][y] = '0'  # Mark as visited
            
            # Visit all 4 neighbors
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an island
                    dfs(i, j)  # Mark the entire island as visited
                    count += 1
        
        return count
    
# BFS
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x, y):
            queue = deque([(x, y)])
            grid[x][y] = '0'  # Mark as visited
            
            while queue:
                cx, cy = queue.popleft()
                
                # Visit all 4 neighbors
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                        queue.append((nx, ny))
                        grid[nx][ny] = '0'  # Mark as visited

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an island
                    bfs(i, j)  # Mark the entire island as visited
                    count += 1
        
        return count
    
"""
Time Complexity
	•	O(m * n):
	•	Each cell is visited once.

Space Complexity
	•	O(m * n):
	•	In the worst case, the recursion stack (DFS) or queue (BFS) contains all cells of the grid.
"""