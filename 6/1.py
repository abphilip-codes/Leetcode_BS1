# 441
# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        while(n>ans):
            ans+=1
            n-=ans
        return ans