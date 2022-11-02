"""
Given an m x n matrix, return all elements of the matrix in spiral order. 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        resL = []
        if len(matrix) == 0:
            return resL
        rowBegin = 0
        colBegin = 0
        rowEnd = len(matrix) - 1
        colEnd = len(matrix[0]) - 1
        while (rowBegin <= rowEnd and colBegin <= colEnd):
            for i in range(colBegin, colEnd+1):
                resL.append(matrix[rowBegin][i])
            rowBegin += 1
            
            for i in range(rowBegin, rowEnd + 1):
                resL.append(matrix[i][colEnd])
            colEnd -= 1
            
            if rowBegin <= rowEnd: # This condition for single row matrix
                for i in range(colEnd, colBegin-1, -1):
                    resL.append(matrix[rowEnd][i])
                rowEnd -= 1
            if colBegin <= colEnd: # This condition for signle column matrix
                for i in range(rowEnd, rowBegin - 1, -1):
                    resL.append(matrix[i][colBegin])
                colBegin += 1
                
        return resL