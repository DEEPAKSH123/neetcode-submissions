class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        visit=set()
        def dfs(i,j):
            if i<0 or j<0 or i==len(grid) or j==len(grid[0]) or (i,j) in visit or grid[i][j]!=1:
                return 0
            visit.add((i,j))
            return 1 + dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visit:
                    ans=max(ans,dfs(i,j))
        return ans
        