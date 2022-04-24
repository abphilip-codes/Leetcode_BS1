# 1523
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + (low % 2) + (high % 2)) // 2