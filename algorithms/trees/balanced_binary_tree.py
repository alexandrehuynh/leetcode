"""
Leetcode 110. Balanced Binary Tree: https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced.

Example 1:
https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0 # base case; height of an empty tree is 0

            left_height = checkHeight(node.left)
            if left_height == -1: # left subtree is unbalanced
                return -1
            
            right_height = checkHeight(node.right)
            if right_height == -1: # right subtree is unbalanced
                return -1

            # check if the current node is balanced
            if abs(left_height - right_height) > 1:
                return -1 # current node is unbalanced

            # return the height of the tree rooted at this node
            return max(left_height, right_height) + 1
        
        return checkHeight(root) != -1  # if the height is -1, the tree is unalanced