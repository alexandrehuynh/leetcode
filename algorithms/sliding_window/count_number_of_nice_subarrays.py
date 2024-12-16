"""
Leetcode 1248. Count Number of Nice Subarrays: https://leetcode.com/problems/count-number-of-nice-subarrays/description/

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
# Sliding Windows Approach
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(nums, k):
            start, result, odd_count = 0, 0, 0

            for end in range(len(nums)):
                # Count the odd numbers in the current window
                if nums[end] % 2 == 1:
                    odd_count += 1
                
                # Shrink the window until there are at most k odd numbers
                while odd_count > k:
                    if nums[start] % 2 == 1:
                        odd_count -= 1
                    start += 1
                
                # Add the number of subarrays ending at 'end'
                result += end - start + 1

            return result

        # Subarrays with exactly k odd numbers
        return atMost(nums, k) - atMost(nums, k - 1)
    
# Prefix Sum
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1  # Base case for prefix sum
        odd_count = 0
        result = 0

        for num in nums:
            # Increment odd_count for each odd number
            if num % 2 == 1:
                odd_count += 1
            
            # Add subarrays ending at this point with exactly k odd numbers
            result += count_map[odd_count - k]
            
            # Increment the count of the current odd_count
            count_map[odd_count] += 1

        return result
    
"""
Approach	    Time Complexity	    Space Complexity	Notes
Sliding Window	O(n)	            O(1)	            Uses two-pointer technique.
Prefix Sum	    O(n)	            O(n)	            Uses hash mapping for prefix sums.
"""