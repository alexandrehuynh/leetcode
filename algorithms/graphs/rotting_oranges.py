"""
994. Rotting Oranges: https://leetcode.com/problems/rotting-oranges/description/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
https://assets.leetcode.com/uploads/2019/02/16/oranges.png

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()  # To store rotten oranges with their time
        fresh_count = 0  # To count the number of fresh oranges

        # Initialize the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # Add rotten orange with time 0
                elif grid[r][c] == 1:
                    fresh_count += 1

        # BFS traversal
        time_elapsed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4-directional movement
        while queue:
            x, y, time = queue.popleft()
            time_elapsed = max(time_elapsed, time)

            # Process adjacent cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2  # Mark orange as rotten
                    queue.append((nx, ny, time + 1))
                    fresh_count -= 1

        # If fresh oranges remain, return -1
        return -1 if fresh_count > 0 else time_elapsed
    
"""
Time Complexity
	•	O(m * n):
	•	Each cell is visited once during BFS.

Space Complexity
	•	O(m * n):
	•	The queue can hold all cells in the grid.
"""