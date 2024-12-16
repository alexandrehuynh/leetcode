"""
Leetcode 207. Course Schedule: https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

# Depth First Search

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()  # Tracks visited nodes
        recursion_stack = set()  # Tracks nodes in the current recursion path

        def dfs(course):
            if course in recursion_stack:  # Cycle detected
                return False
            if course in visited:  # Already fully processed
                return True

            # Mark the course as visited and add it to the recursion stack
            recursion_stack.add(course)

            # Check all neighbors
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Remove the course from the recursion stack and mark as fully processed
            recursion_stack.remove(course)
            visited.add(course)

            return True

        # Check all courses
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
    
# Topological Sort (Kahn's Algorithm)
from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list and in-degree array
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize the queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        completed_courses = 0

        while queue:
            course = queue.popleft()
            completed_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are completed, no cycle exists
        return completed_courses == numCourses
    
"""
Approach	            Time Complexity	    Space Complexity	Notes
DFS (Cycle Detection)	O(V + E)	        O(V + E)	        Simple recursion-based approach.
Topological Sort	    O(V + E)	        O(V + E)	        Iterative and intuitive for cycles.
"""