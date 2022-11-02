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