""" Something reverse related means two pointer may be used.
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

"""


class Solution:
    
        def reverseVowels(self, s: str) -> str:
            sl = list(s)
            vowels = "aeiouAEIOU"
            start = 0
            end = len(s) - 1
            while start < end:
                while start < len(sl) and sl[start] not in vowels:
                    start += 1
                while end > 0 and sl[end] not in vowels:
                    end -= 1
                if(start < end):
                    sl[start], sl[end] = sl[end], sl[start]
                    start += 1
                    end -= 1
            return ''.join(sl)

"""    
    def reverseVowels(self, s: str) -> str:
    # Using this function gives TLE because it makes the string to list every time it swaps
    def swap(i, j, s) -> str:
        strList = list(s)
        strList[i], strList[j] = strList[j], strList[i] 
        return ''.join(strList)

    vowels = "aeiouAEIOU"
    start = 0
    end = len(s) - 1
    while start < end:
        while start < len(s) and s[start] not in vowels:
            start += 1
        while end > 0 and s[end] not in vowels:
            end -= 1
        if(start < end):
            s = swap(start, end, s)
            start += 1
            end -= 1
    return s
"""      
