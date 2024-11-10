"""
Leetcode 226. Invert Binary Tree: https://leetcode.com/problems/invert-binary-tree/description/

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:
https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg

Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # swap the left and right children
        root.left, root.right = root.right, root.left

        # recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
"""
For LeetCode's Invert Binary Tree, the DFS approach (recursive) is commonly used and straightforward. 
However, BFS is also a viable and sometimes preferable solution, especially if you want to avoid recursion.

Which Algorithm to Choose?
DFS (Recursive): This is often the preferred solution for inverting a binary tree because it’s concise and leverages recursion to process each node.
BFS (Iterative): Use this if you want an iterative solution or if you're working with a large tree where recursion might lead to stack overflow 
(though Python’s recursion depth limit is usually sufficient for typical binary trees).
"""