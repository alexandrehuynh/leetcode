"""
Leetcode 271: Encode and Decode Strings: https://neetcode.io/problems/string-encode-and-decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""
class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> list[str]:
        """
        Decodes a single string to a list of strings.
        """
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter #
            j = s.find("#", i)
            # Get the length of the next string
            length = int(s[i:j])
            # Extract the string of the given length
            decoded.append(s[j + 1 : j + 1 + length])
            # Move to the next part of the encoded string
            i = j + 1 + length
        return decoded