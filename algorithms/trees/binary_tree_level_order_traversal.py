"""
Leetcode 102. Binary Tree Level Order Traversal: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Return an empty list if the tree is empty

        result = []  # Final list to store level order traversal
        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            level = []  # Temporary list to store the values of the current level
            level_size = len(queue)  # Number of nodes at the current level

            for _ in range(level_size):
                node = queue.popleft()  # Remove the front node from the queue
                level.append(node.val)  # Add the node's value to the current level

                # Add the node's children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)  # Append the current level to the result

        return result
    
"""
Time Complexity
	•	O(n): Every node is processed once.

Space Complexity
	•	O(n): At most, the queue holds all nodes at the largest level (worst case: balanced binary tree).
"""