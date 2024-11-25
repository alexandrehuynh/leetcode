"""
Leetcode 543. DIameter of Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/description/Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
# Depth-First Search 

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0  # Initialize the maximum diameter

        def dfs(node):
            if not node:
                return 0  # Height of a null node is 0

            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update the diameter at this node
            self.diameter = max(self.diameter, left_height + right_height)

            # Return the height of the node
            return 1 + max(left_height, right_height)

        dfs(root)  # Start DFS traversal from the root
        return self.diameter
    
    # Space Complexity: O(h), where h is the height of the tree
        # •	The recursion stack will use space proportional to the height of the tree.
        # •	In the worst case (skewed tree), h = n → O(n).
        # •	In the best case (balanced tree), h = log(n) → O(log(n)).
    
    # Time Complexity: O(n), where n is the number of nodes in the tree.