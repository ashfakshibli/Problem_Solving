"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = [0]*26
        for ch in s:
            #print(ord(ch) - ord('a'))
            if seen[ord(ch) - ord('a')] == 0:
                seen[ord(ch) - ord('a')] = 1
            else:
                seen[ord(ch) - ord('a')] += 1
        for ch in t:
            if seen[ord(ch) - ord('a')] == 0:
                return False
            seen[ord(ch) - ord('a')] -= 1
        for i in range(0,26):
            if seen[i] != 0:
                return False
        return True