# 1855
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        z, y = 0, 0
        while(z<len(nums1) and y<len(nums2)):
            if(nums1[z]>nums2[y]): z+=1
            elif(nums1[z]<=nums2[y]):
                ans = max(ans, y-z)
                y+=1
        return ans