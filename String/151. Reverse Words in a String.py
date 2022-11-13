"""
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

"""


# reverse the whole string and then each word
"""

class Solution:
    def trimSpaces(self, s: str)-> list:
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
                left += 1
        while left <= right and s[right] == ' ':
                right -= 1
        output = []
        while left <= right:
            # add until a space found
            if s[left] != ' ':
                output.append(s[left])
            # if space, ignore expect one space
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output
            
    def reverse(self, stl: list, l:int, r:int) -> None:
        while l <= r:
            stl[l], stl[r] = stl[r], stl[l]
            l, r = l+1, r-1
            
    def reverse_words(self, stl: list):
        n = len(stl)
        start, end = 0,0
        
        while start<n:
            while end < n and stl[end] != ' ':
                end += 1
            self.reverse(stl, start, end-1)
            start = end+1
            end += 1
        
            
        
    def reverseWords(self, s: str) -> str:
        # Python strings are immutable. Convert to char array.
        strl = self.trimSpaces(s) 
        self.reverse(strl, 0, len(strl)-1)
        self.reverse_words(strl)
        return ''.join(strl)

"""

# Deque solution
class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove extra spaces around
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
                left += 1
        while left <= right and s[right] == ' ':
                right -= 1
                
        d, word = deque(), []
        
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        return ' '.join(d)
        
#Pythonic simple solution
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
"""
