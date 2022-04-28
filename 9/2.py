# 1346
# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        k = 0   
        for z in arr:
            if(z*2 in arr and z): return True
            elif not z: k+=1
        return True if(k>1) else False