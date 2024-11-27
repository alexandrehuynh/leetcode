"""
Leetcode 217. Contains Duplicate: https://leetcode.com/problems/contains-duplicate/description/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]

Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]

Output: false

Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Initialize an empty set to store unique elements
        
        for num in nums:
            if num in seen:  # If the number is already in the set, we found a duplicate
                return True
            seen.add(num)  # Otherwise, add the number to the set
        
        return False  # If no duplicates are found, return False

# Time Complexity: O(n) 
#   The algorithm iterates through the list once, and set operations (add and check) are O(1) on average.

# Space Complexity: O(n) 
#   The space required to store the seen set is proportional to the size of the input array in the worst case (when all elements are distinct).