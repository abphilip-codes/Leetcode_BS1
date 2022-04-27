# 278
# https://leetcode.com/problems/first-bad-version/

class Solution:
    def mySqrt(self, x: int) -> int:
        if(x<2): return x
        l, r = 2, x//2
        while(l<=r):
            mid = l+(r-l)//2
            s = mid**2
            if(s==x): return mid
            elif(s<x): l = mid+1
            elif(s>x): r = mid-1 
        return r