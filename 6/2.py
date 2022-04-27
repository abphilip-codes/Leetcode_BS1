# 1539
# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while(l<=r):
            m = l+(r-l)//2
            if(arr[m]-m-1>=k): r = m-1
            elif(arr[m]-m-1<k): l = m+1
        return arr[r]+(k-(arr[r]-(r)-1))