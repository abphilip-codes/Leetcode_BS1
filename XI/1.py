# 1855
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1)&Counter(nums2)).elements())