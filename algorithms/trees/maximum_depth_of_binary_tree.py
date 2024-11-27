"""
Leetcode 104. Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
from typing import Optional

# DFS (Recursive)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the node doesn't exist, return 0
        if not root:
            return 0
        
        # Recursively find the max depth of left and right subtrees
        # Use self to refer to the maxDepth method of the same instance
        left_depth = self.maxDepth(root.left) 
        right_depth = self.maxDepth(root.right)
        
        # The max depth of the current node is 1 plus the max of the depths of its children
        return 1 + max(left_depth, right_depth)
    
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
# 	•	The recursion stack can grow as large as the height of the tree.
# 	•	For a balanced tree, this is O(log n). For a skewed tree, this is O(n).

# BFS (Iterative)
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0  # If the tree is empty, the depth is 0
        
        queue = deque([root])  # Initialize the queue with the root node
        depth = 0  # Depth counter
        
        while queue:
            depth += 1  # Increment depth at each level
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)  # Add left child to the queue
                if node.right:
                    queue.append(node.right)  # Add right child to the queue
        
        return depth  # Return the final depth
    
# Time Complexity: O(n), where n is the number of nodes in the tree.
#   •	Each node is processed once.
# Space Complexity: O(w), where w is the maximum width of the tree.
#   •	The queue holds all nodes at the current level. In the worst case (balanced tree), the width is approximately n/2, so the space complexity is O(n).