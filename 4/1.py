# 35
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for z in range(len(nums)):
                if(nums[z]>target): return z
                if(z==len(nums)-1): return z+1 