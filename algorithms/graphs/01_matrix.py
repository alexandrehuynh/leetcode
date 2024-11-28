"""
Leetcode 542. 01 Matrix: https://leetcode.com/problems/01-matrix/description/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
# Breadth-First Search (BFS) Approach

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])  # Dimensions of the matrix
        queue = deque()  # Queue for BFS
        distances = [[float('inf')] * n for _ in range(m)]  # Initialize distances with infinity

        # Step 1: Initialize the queue with all '0' positions and set their distances to 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    distances[i][j] = 0  # Distance to itself is 0

        # Step 2: Perform BFS
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        while queue:
            x, y = queue.popleft()

            # Check all 4 neighbors
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                # If within bounds and a shorter distance is found
                if 0 <= new_x < m and 0 <= new_y < n:
                    if distances[new_x][new_y] > distances[x][y] + 1:
                        distances[new_x][new_y] = distances[x][y] + 1
                        queue.append((new_x, new_y))  # Add the neighbor to the queue

        return distances

# Time Complexity: O(m * n)
# 	•	Each cell is processed at most once during the BFS traversal.

# Space Complexity: O(m * n)
# 	•	Space is used for the distances matrix and the BFS queue.