# 74
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = bisect_left(matrix, target, key = lambda z:z[-1])
        return (k<len(matrix) and matrix[k][bisect_left(matrix[k],target)]==target)