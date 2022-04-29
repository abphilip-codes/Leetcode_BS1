# 1855
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for z in range(len(nums1)):
            l, r = z, len(nums2)-1
            while(l<=r):
                mid = (l+r)//2
                if(nums1[z]<=nums2[mid]):
                    l = mid+1
                    if((mid-z)>ans): ans = mid-z
                elif(nums1[z]>nums2[mid]): r = mid-1
        return ans