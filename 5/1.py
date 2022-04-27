# 278
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r, ans = 1, n, None
        while(l<=r):
            mid = (l+r)//2
            if not isBadVersion(mid): l = mid+1
            else: r, ans = mid-1, mid
        return ans