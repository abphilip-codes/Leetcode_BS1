# 633
# https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while(l<=r):
            k = l**2 + r**2
            if(k==c): return True
            elif(k<c): l+=1
            elif(k>c): r-=1
        return False