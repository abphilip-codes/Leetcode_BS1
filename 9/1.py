# 1337
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans, h = [], []
        for z in range(len(mat)): heappush(h, (sum(mat[z]), z))
        for z in range(k): 
            a, b = heappop(h)
            ans.append(b)
        return ans