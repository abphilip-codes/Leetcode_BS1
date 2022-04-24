# 374
# https://leetcode.com/problems/guess-number-higher-or-lower/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + (low % 2) + (high % 2)) // 2