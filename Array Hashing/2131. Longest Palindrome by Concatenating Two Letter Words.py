"""
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters."""

from typing import Counter, List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # a count variable contains the number of occurrences of each word
        # Coounter makes hashmap of word -> count
        countW = Counter(words)
        answer = 0
        # if palidrome words cunt is odd number then one can be placed in center.
        central = False
        for word, countOfWord in countW.items():
             # if the word itself is a palindrome
            if word[0] == word[1]:
                if countOfWord % 2 == 0:
                    answer += countOfWord
                else: 
                    answer += countOfWord - 1
                    central = True
            # for not palindrome words.
            # reverse one will be considered and minmimum
            # if ab is word ba is reversed one.
            elif word[0] < word[1]:
                answer += 2 * min(countOfWord, countW[word[1] + word[0]])
        if central:
            answer += 1
        return 2 * answer