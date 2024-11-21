"""
Leetcode 206. Reverse Linked List: https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_temp = current.next  # Temporarily store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev to the current node
            current = next_temp       # Proceed to the next node
        return prev  # prev will be the new head of the reversed list

# Time Complexity: O(n)
# Space Complexity: O(1)