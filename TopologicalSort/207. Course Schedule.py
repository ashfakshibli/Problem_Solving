"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""



from typing import Deque, List


class Solution:
    def makeAdjacencyList(edgeL: List[List[int]], n):
        ajacencyL = [[] for _ in range(n)]
        for c1, c2 in edgeL:
                ajacencyL[c2].append(c1)
        return ajacencyL
        
    def topoBFS(self, numNodes, edgeList):
        # 1. A list stores No. of incoming edges of each vertex
        self.makeAdjacencyList(edgeList, numNodes)
        
        indegrees = [0]* numNodes
        for v1, v2 in edgeList:
            # v2v1 form a directed edge
            indegrees[v1] += 1
        
        # 2. a queue of all vertices with no incoming edge
        # at least one such node must exist in a non-empty acyclic graph
        # vertices in this queue have the same order as the eventual topological
        # sort
        queue = Deque([int]) # Deque always helps better than a queue
        for i in range(numNodes):
            if indegrees[i] == 0: # as said taking anvertex which has no indegree
                queue.append(i)
        
        # count of visiting vertices
        countV = 0 
        #the topological sorted (reverse) list when there is no indegree of a vertex
        topoOrder = []
        
        while queue:
            #a. pop a vertex from front of queue
            # depending on the order that vertices are removed from queue,
            # a different solution is created
            cur = queue.popLeft()
            # b. append it to topoOrder
            topoOrder.append(cur)
            countV += 1
            # for each descendant of current vertex, reduce its in-degree by 1
            for edge in edgeList[cur]:
                indegrees[edge] -= 1
                # if in-degree becomes 0, add it to queue
                if(indegrees[edge] == 0):
                    topoOrder.append(edge)
        
        if countV != numNodes:
            return None # graph has atleast one cycle. Every node could not be visited for that reason.
        else:
            return topoOrder
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True if self.topoBFS(numCourses, prerequisites) else False
        
        
        


