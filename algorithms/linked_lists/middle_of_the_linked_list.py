"""
Leetcode 876. Middle of the Linked List: https://leetcode.com/problems/middle-of-the-linked-list/description/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
 
Example 1:
https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head  # Initialize both pointers at the head of the list
        
        while fast and fast.next:
            slow = slow.next       # Move slow pointer by 1 step
            fast = fast.next.next  # Move fast pointer by 2 steps

        return slow  # When fast reaches the end, slow is at the middle
    
# Time Complexity: 0(n)
# Space Complexity: 0(1)