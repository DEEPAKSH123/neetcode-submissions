from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visit=set()
        @cache
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or (i,j) in visit:
                return 0
            if i==m-1 and j==n-1:
                return 1
            visit.add((i,j))
            ans = dfs(i+1,j) + dfs(i,j+1)
            visit.remove((i,j))
            return ans
        return dfs(0,0)
        