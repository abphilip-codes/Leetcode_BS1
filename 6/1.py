# 441
# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if(n==1): return 1
        l, r = 1, n
        while(l<r):
            m = (l+r)//2
            if((m*(m+1))//2>n): r = m
            else: l = m+1
        return l-1