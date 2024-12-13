"""
Leetcode 133. Clone Graph: https://leetcode.com/problems/clone-graph/description/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
https://assets.leetcode.com/uploads/2020/01/07/graph.png

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
"""

# Using DFS (Recursive)

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None  # If the graph is empty, return None

        clones = {}  # Dictionary to map original nodes to their clones

        def dfs(node):
            if node in clones:
                return clones[node]  # Return the clone if it already exists
            
            # Create a clone for the current node
            clone = Node(node.val)
            clones[node] = clone

            # Recursively clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)  # Start the DFS traversal from the given node
    
# Using BFS
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None  # If the graph is empty, return None

        clones = {node: Node(node.val)}  # Dictionary to map original nodes to their clones
        queue = deque([node])  # Queue for BFS

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in clones:
                    # Create a clone for the neighbor if it doesn't exist
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Add the clone of the neighbor to the current node's clone
                clones[current].neighbors.append(clones[neighbor])

        return clones[node]  # Return the clone corresponding to the input node

"""
Time Complexity
	•	O(V + E):
	•	Each node (V) and edge (E) is visited once during traversal.

Space Complexity
	•	O(V):
	•	The dictionary clones stores one entry per node.
	•	The recursion stack in DFS or queue in BFS can grow up to O(V).
"""