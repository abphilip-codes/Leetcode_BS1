# 1608
# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for z in letters:
        #     if(ord(z)>ord(target)): return z
        # else: return letters[0]
        l, r = 0, len(letters)-1
        ans = letters[0]
        while(l<=r):
            mid = l+(r-l)//2
            if(ord(letters[mid])<=ord(target)): l = mid+1
            else: ans, r = letters[mid], mid-1
        return ans