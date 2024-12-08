"""
Leetcode 973. K Closest Points to Origin: https://leetcode.com/problems/k-closest-points-to-origin/description/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Explanation:

The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]

Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""
# Python Implementation: Using a Max-Heap

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a max-heap to store the k closest points
        max_heap = []

        for x, y in points:
            # Calculate the squared distance to the origin
            distance = -(x**2 + y**2)  # Use negative for max-heap behavior
            if len(max_heap) < k:
                heapq.heappush(max_heap, (distance, [x, y]))
            else:
                # If the current point is closer than the farthest point in the heap
                heapq.heappushpop(max_heap, (distance, [x, y]))

        # Extract the points from the heap and return them
        return [point for _, point in max_heap]
    
"""
Time Complexity
	Heap Operations:
	•	For each point: O(log k) to push into the heap.
	•	For n points: O(n log k).

Space Complexity
	•	O(k): The heap stores at most k points.
    """

# Python Implementation: Using Sorting
 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort points by squared distance
        points.sort(key=lambda point: point[0]**2 + point[1]**2)
        # Return the first k points
        return points[:k]
    
"""
Time Complexity:
	•	Sorting takes O(n log n).

Space Complexity:
	•	O(n): For the sorting operation.
"""