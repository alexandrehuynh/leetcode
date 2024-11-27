"""
Leetcode 67. Add Binary: https://leetcode.com/problems/add-binary/description/

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []  # To store the binary result
        carry = 0  # Initialize carry to 0

        # Start from the last digit of both strings
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            # Get the current digits, default to 0 if index out of bounds
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Add the digits along with the carry
            total = digit_a + digit_b + carry
            carry = total // 2  # Carry is the integer division of total by 2
            result.append(str(total % 2))  # Append the remainder (0 or 1)

            # Move to the next digits
            i -= 1
            j -= 1

        # The result is built in reverse order, so reverse it at the end
        return ''.join(reversed(result))
    
    # Time Complexity O(max(n, m)), where:
	    # •	n is the length of string a.
	    # •	m is the length of string b.
    # Space Complexity: O(max(n, m))

    # easier solutioon with bin()
    class Solution:
        def addBinary(self, a: str, b: str) -> str:
            return bin(int(a, 2) + int(b, 2))[2:]
    
    # Time Complexity O(n + m)
    # Space Complexity O(n + m)
