"""
Leetcode 53. Maximum Subarray: https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max_sum to the first element
        current_sum = nums[0]  # Initialize current_sum to the first element
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])  # Update the current subarray sum
            max_sum = max(max_sum, current_sum)  # Update the maximum sum encountered so far
        
        return max_sum
    
# Time Complexity: 0(n)
# 	• We iterate through the array once to calculate the maximum subarray sum.

# Space Complexity: 0(1)
# 	• Only constant extra space is used for current_sum and max_sum.