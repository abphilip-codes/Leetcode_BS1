# 1385
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def bs(l,r,arr,k1,k2):
            while l<=r:
                mid=(l+r)//2 
                if(k1<=arr[mid]<=k2): return True
                elif arr[mid]>k2: r=mid-1
                else: l=mid+1 
            return False 
        
        n=len(arr2)
        c=0
        for ele in arr1:
            if not bs(0,n-1,arr2,ele-d,ele+d): c+=1
        return c