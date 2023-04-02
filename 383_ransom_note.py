"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote."""

# Problem Explanation
"""The ransom note can be constructed from the magazine if and only if the frequency of each character in the ransom note is less than or equal to the frequency of that character in the magazine.

For example, if ransomNote = "aa" and magazine = "aab", we can construct the ransom note from the magazine because the frequency of both characters 'a' is less than or equal to the frequency of that character in the magazine.

"""

# Examples
"""
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true


"""

# Constraints
"""
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# Code

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                magazine = magazine.replace(i, "", 1)
        return True
    




