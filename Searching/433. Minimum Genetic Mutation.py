"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
"""



from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def checkNh(a, b):
            return sum([1 for i in range(len(b)) if a[i]!=b[i]]) == 1
        
        # We have to BFS our way to start to end.
        # Take queue and seen set for BFS
        q = deque([[start, 0]])
        seen = {start}
        while q:
            # take deque left object 
            cur, mutations = q.popleft()
            # if current object is the last one return the mutation count
            if cur == end:
                return mutations
            # Check in bank if the neighbour exists
            for nh in bank:
                # if neighbour exist but not visited append in deque and seen set
                if checkNh(nh, cur) and nh not in seen:
                    q.append([nh, mutations+1])
                    seen.add(nh)
            
            """
            # Alternative way to create every possible mutation and check with bank
            # More time consuming
            for c in "ACGT":
                for i in range(len(cur)):
                    nh = cur[:i] + c + cur[i+1:]
                    if nh not in seen and nh in bank:
                        q.append([nh, mutations+1])
                        seen.add(nh)
            """

        return -1