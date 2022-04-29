# 153
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1)&Counter(nums2)).elements())