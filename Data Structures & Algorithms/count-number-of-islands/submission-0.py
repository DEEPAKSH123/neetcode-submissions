class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        co=0
        visit=set()
        def dfs(r,c):
            if r<0 or c<0 or r==row or c==col or (r,c) in visit or grid[r][c]=="0":
                return
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r-1,c)
            
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and (r,c) not in visit:
                    dfs(r,c)
                    co+=1
        return co


        