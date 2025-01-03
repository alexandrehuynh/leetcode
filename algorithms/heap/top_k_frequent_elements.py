"""
Leetcode. 347. Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
""" 
# Min-Heap
from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        freq_map = Counter(nums)
        
        # Use a min-heap to store the top k elements
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))  # Push frequency first
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the smallest frequency
        
        # Extract elements from the heap
        return [num for freq, num in heap]
    
# Sorting
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        freq_map = Counter(nums)
        
        # Sort elements by frequency and pick the top k
        return [item for item, freq in freq_map.most_common(k)]

# Bucket Sort
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        freq_map = Counter(nums)
        
        # Create buckets where index represents frequency
        max_freq = max(freq_map.values())
        bucket = [[] for _ in range(max_freq + 1)]
        
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        # Get the top k elements from the buckets
        result = []
        for freq in range(len(bucket) - 1, 0, -1):  # Iterate from high to low frequency
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result
                
# the one I wrote
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            if num in freq:
                freq[num] += 1
            # else:  I dont need this because of defaultdict
            #     freq[num] = 1
        
        heap = []

        for element, frequency in freq.items():
            heapq.heappush(heap, (frequency, element))

            if len(heap) > k:
                heapq.heappop(heap)
            
        return [element for frequency, element in heap]