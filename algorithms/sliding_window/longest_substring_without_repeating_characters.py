"""
Leetcode 3. Longest Substring Without Repeating Characters:

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
# using a set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store characters in the current window
        max_length = 0  # Maximum length of substring
        start = 0  # Left pointer of the sliding window

        for end in range(len(s)):  # Right pointer of the sliding window
            # If the character is already in the set, shrink the window
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1  # Move the left pointer to the right

            # Add the current character to the set
            char_set.add(s[end])
            # Update the maximum length of the window
            max_length = max(max_length, end - start + 1)

        return max_length
    
"""
Time Complexity
	•	O(n): Each character is added to and removed from the set at most once.

Space Complexity
	•	O(min(n, m)):
	•	n is the length of the string.
	•	m is the size of the character set (e.g., 26 for lowercase letters).
"""

# using a dictionary
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Dictionary to store the last index of each character
        max_length = 0
        start = 0  # Left pointer of the sliding window

        for end in range(len(s)):  # Right pointer of the sliding window
            if s[end] in char_index:
                # Move the start pointer to the right of the last occurrence of s[end]
                start = max(start, char_index[s[end]] + 1)

            # Update the last index of the character
            char_index[s[end]] = end
            # Update the maximum length
            max_length = max(max_length, end - start + 1)

        return max_length
    
"""
Time Complexity
	•	O(n): Each character is added to and removed from the set at most once.

Space Complexity
	•	O(min(n, m)):
	•	n is the length of the string.
	•	m is the size of the character set (e.g., 26 for lowercase letters).
"""