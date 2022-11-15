# 947. Most Stones Removed with Same Row or Column
"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 10^4
No two stones are at the same coordinate point.

"""


"""
class Solution:
    def removeStones(self, points):
        unionFind = {}
        def find(x):
            if x != unionFind[x]:
                unionFind[x] = find(unionFind[x])
            return unionFind[x]
        def union(x, y):
            unionFind.setdefault(x, x)
            unionFind.setdefault(y, y)
            unionFind[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in unionFind})
    
 """   
    

#Detail Explained Code


class Solution:
    def removeStones(self, stones):
        
        ### UF is a hash map where you can find the root of a group of elements giving an element.
        ### A key in UF is a element, UF[x] is x's parent.
        ### If UF[x] == x meaning x is the root of its group.
        UF = {}
        
        ### Given an element, find the root of the group to which this element belongs.
        def find(x):
            
            ### If x == UF[x], meaning x is the root of this group.
            ### If x != UF[x], we use the find function again on x's parent UF[x] 
            ### until we find the root and set it as the parent (value) of x in UF.
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        ### Given two elements x and y, we know that x and y should be in the same group, 
        ### this means the group that contains x and the group that contains y 
        ### should be merged together if they are currently separate groups.
        ### So we first find the root of x and the root of y using the find function.
        ### We then set the root of y (rootY) as the root of the root of x (rootX).
        def union(x, y):
            
            ### this may be the first time we see x or y, so set itself as the root.
            if x not in UF:
                UF[x] = x
            if y not in UF:
                UF[y] = y
            rootX = find(x)
            rootY = find(y)
            # set the root of y (rootY) as the root of the root of x (rootX)
            UF[rootX] = rootY
        
        ### The main reason we can use the union-find algorithm here is that we treat the x and y of each stone as a single element!
        ### DO NOT think of a stone as (x,y); instead, think about one stone as two elements, x and y!
        ### Now, a stone means two elements, x and y, that are CONNECTED.
        ### Since x and y can be the same, but 0 <= x, y <= 10^4, we can add 10^4 to every y 
        ### to distinguish x and y and treat them as different elements.
        ### We can go to every pair of x and y (a stone), we know that x and y should be in 
        ### the same group, so we union them.
        maxX = 10**4
        for x,y in stones:
            union(x,y+maxX)
        
        ### Finally, we go through each element in UF and find their root, count how many 
        ### connected components (unique roots) are there and subtract it from the total 
        ### number of stones.
        return len(stones) - len({find(n) for n in UF})