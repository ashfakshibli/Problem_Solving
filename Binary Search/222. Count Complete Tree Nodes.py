"""
222. Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Enumerate potential nodes in the last level from 0 to 2^d - 1. How to check if the node number idx exists? Let's use binary search again to reconstruct the sequence of moves from root to idx node. For example, idx = 4. idx is in the second half of nodes 0,1,2,3,4,5,6,7 and hence the first move is to the right. Then idx is in the first half of nodes 4,5,6,7 and hence the second move is to the left. The idx is in the first half of nodes 4,5 and hence the next move is to the left. The time complexity for one check is O(d).

"""
    def exists(self, node: TreeNode, d: int, idx: int)-> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        l, r = 0, 2**d - 1
        for _ in range(d):
            pivot = l + (r-l)//2
            if pivot >= idx:
                node = node.left
                r = pivot
            else:
                node = node.right
                l = pivot+1
        return node is not None
        
        
    def getDepth(self, node: TreeNode):
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        d = self.getDepth(root)
        
        # if the tree contains 1 node
        if d == 0:
            return 1
        
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        l, r = 0, 2**d - 1
        while l<=r:
            pivot = l + (r-l)//2
            if self.exists(root, d, pivot):
                l = pivot + 1
            else:
                r = pivot - 1
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        
        return 2**d - 1 + l
                
            
            