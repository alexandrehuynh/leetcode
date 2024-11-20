"""
Leetcode 383. Ransom Note: https://leetcode.com/problems/ransom-note/description/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count character frequencies in magazine
        magazine_count = Counter(magazine)
        
        # Check if ransomNote can be constructed
        for char in ransomNote:
            if magazine_count[char] > 0:
                magazine_count[char] -= 1  # Use one occurrence of the character
            else:
                return False  # Not enough characters to construct ransomNote
        
        return True
    
# without using counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Use a dictionary to count characters in the magazine
        char_count = {}
        
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Check if ransomNote can be constructed
        for char in ransomNote:
            if char_count.get(char, 0) == 0:
                return False  # Not enough characters
            char_count[char] -= 1  # Use one occurrence of the character
        
        return True