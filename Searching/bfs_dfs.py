from collections import deque
from typing import Dict, Set

graph = {
    0 : [1,6],
    1 : [0,2,3],
    2 : [1,4],
    3 : [1,4,5],
    4 : [2,3,5],
    5 : [3,4],
    6 : [0]
}


def dfs(graph: Dict[int, list[int]], cur: int, visited: Set[int]):
    if cur in visited: return
    visited.add(cur)
    print(cur, end = " ")
    for i in graph[cur]:
        dfs(graph, i, visited)

def bfs(graph: Dict[int, list[int]], node: int):
    q = deque([node])
    visited = set([node])
    while q:
        cur = q.popleft()
        print(cur, end = " ")
        for next in graph[cur]:
            if next in visited: continue
            visited.add(next)
            q.append(next)

"""
            1 - 0 - 6
           / \
          2   3
           \ / \
            4 - 5  
"""



print("By dfs: ", end=" ")
dfs(graph, 2, set())
print("\nBy bfs: ", end=" ")
bfs(graph, 2)