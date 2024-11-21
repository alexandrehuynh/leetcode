"""
Leetcode 21. Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
 
Example 1:
https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a prehead node
        prehead = ListNode(-1)
        
        # Initialize the current node to prehead
        current = prehead
        
        # While both lists are not empty
        while list1 and list2:
            # Compare the values and advance the pointers accordingly
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remainder of list1 or list2
        current.next = list1 if list1 is not None else list2
        
        # Return the merged list, which starts from prehead.next
        return prehead.next
        