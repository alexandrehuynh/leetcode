"""
Leetcode 49. Group Anagram: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

# using sorted strings as key
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Dictionary to store grouped anagrams

        for word in strs:
            # Create the "signature" by sorting the word
            signature = ''.join(sorted(word))
            # Add the word to the corresponding group
            anagrams[signature].append(word)

        # Return all grouped anagrams
        return list(anagrams.values())
    
"""
Time Complexity
	1.	Sorting each word takes O(k log k), where k is the length of the word.
	2.	Iterating through all n words takes O(n) * O(k log k) → O(n * k log k).

Space Complexity
	1.	The dictionary stores all words → O(n * k), where n is the number of words and k is the average length.
	2.	Sorting each word uses O(k) space for the sorted string.
	•	Total space complexity: O(n * k).
"""
    
# creating a frequency counter
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Dictionary to store grouped anagrams

        for word in strs:
            # Create a "signature" by counting character frequencies
            count = [0] * 26  # Assume only lowercase letters
            for char in word:
                count[ord(char) - ord('a')] += 1
            signature = tuple(count)  # Convert count list to a tuple

            # Add the word to the corresponding group
            anagrams[signature].append(word)

        # Return all grouped anagrams
        return list(anagrams.values())
"""
Time Complexity
	1.	Counting frequencies for each word: O(k).
	2.	Iterating through all words: O(n) * O(k) → O(n * k).

Space Complexity
	1.	The dictionary stores all words → O(n * k).
	2.	Character frequency array → O(26) ≈ O(1).
"""