"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Only min lenth string can be longest common prefix
        shortest = min(strs, key = len)
        ## TODO- Improvement using Binary search
        for i, ch in enumerate(shortest):
            # check with every remaining strs which point they don't match
            for remainStr in strs: 
                if remainStr[i] != ch:
                    #return till it matched
                    return shortest[:i]
        return shortest