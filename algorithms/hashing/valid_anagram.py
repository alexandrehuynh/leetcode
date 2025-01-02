"""
Leetcode 242. Valid Anagram: https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# hash map
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

"""
Time Complexity:
Counting characters: O(n), where n is the length of the strings.
Comparing two dictionaries: O(n).
Space Complexity:
O(n): Space for the frequency dictionary.
"""

# sort
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

"""
Time Complexity:
Sorting both strings: O(n log n), where n is the length of the strings.
Space Complexity:
O(n): Space required to store the sorted strings.
"""

# manual hash map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def manual_counter(s):
            char_count = {}
            for char in s:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            return char_count
                   
        return manual_counter(s) == manual_counter(t)


