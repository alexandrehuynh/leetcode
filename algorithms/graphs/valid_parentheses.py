"""
Leet Code 2. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_brackets.values():  # if it's an opening bracket
                stack.append(char)
            elif char in matching_brackets:  # if it's a closing bracket
                if not stack or stack.pop() != matching_brackets[char]:
                    return False
        
        return not stack  # stack should be empty if all brackets matched