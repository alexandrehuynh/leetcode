"""
Leetcode 409: Longest palindrome: https://leetcode.com/problems/longest-palindrome/description/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count the frequency of each character
        char_count = Counter(s)
        
        length = 0
        odd_found = False
        
        # Iterate through character frequencies
        for count in char_count.values():
            if count % 2 == 0:
                length += count  # Add even counts fully
            else:
                length += count - 1  # Add the largest even part
                odd_found = True  # Mark that we found an odd
        
        # Add 1 if any odd character can be used as the center
        if odd_found:
            length += 1
        
        return length