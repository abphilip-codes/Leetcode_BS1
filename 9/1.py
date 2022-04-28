# 1337
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while(l<r):
            if(numbers[l]+numbers[r]==target): return [l+1, r+1]
            elif(numbers[l]+numbers[r]<target): l+=1
            elif(numbers[l]+numbers[r]>target): r-=1
        return [-1,-1]