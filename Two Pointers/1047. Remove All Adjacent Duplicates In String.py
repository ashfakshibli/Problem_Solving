"""You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters."""

#2 Pointer Solution
class Solution:
    def removeDuplicates(self, s: str) -> str:
        sl = list(s)
        i = 0
        for j in range(len(sl)):
            sl[i] = sl[j]
            if i > 0 and sl[i] == sl[i-1]:
                i -= 2
            #print("i=", i,"list:",sl[:i])
            #print("j=",j,"list:", sl[:j])            
            i += 1
        return ''.join(sl[:i])
            
            


#Stack Solution
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
"""