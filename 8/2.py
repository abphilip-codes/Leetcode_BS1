# 74
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if(n<=nums[0]): return n
        l, r = 0, n
        while(l<=r):
            mid = (l+r)//2
            ans = sum([1 if(nums[z]>=mid) else 0 for z in range(n)])
            if(ans==mid): return ans
            elif(ans<mid): r = mid-1
            elif(ans>mid): l = mid+1
        return -1