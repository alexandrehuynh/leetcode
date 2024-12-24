"""
Leetcode 155. Min Stack: https://leetcode.com/problems/min-stack/description/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""
class MinStack:
    def __init__(self):
        self.stack = []      # Main stack to store elements
        self.min_stack = []  # Stack to track minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the minimum of val and the current min onto the min_stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()  # Remove from the main stack
        self.min_stack.pop()  # Remove from the min_stack

    def top(self) -> int:
        return self.stack[-1]  # Return the top element of the main stack

    def getMin(self) -> int:
        return self.min_stack[-1]  # Return the top element of the min_stack
    
"""
Time Complexity
	•	All operations (push, pop, top, getMin) are O(1).

Space Complexity
	•	O(n): Both stack and min_stack store all elements.
"""