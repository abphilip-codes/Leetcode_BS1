# 1351
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(bisect.bisect_left(z[::-1], 0) for z in grid)