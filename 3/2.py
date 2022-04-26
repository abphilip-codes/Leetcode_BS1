# 1385
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        def bs(l,r,arr,k1,k2):
            while(l<=r):
                mid = (l+r)//2 
                if(k1<=arr[mid]<=k2): return True
                elif(arr[mid]>k2): r = mid-1
                elif(arr[mid]<k1): l = mid+1 
            return False 
        n, c = len(arr2), 0
        for z in arr1:
            if not bs(0,n-1,arr2,z-d,z+d): c+=1
        return c