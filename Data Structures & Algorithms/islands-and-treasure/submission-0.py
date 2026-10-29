import math
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf=math.pow(2,31)-1
        row,col=len(grid),len(grid[0])
        res=grid.copy()
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            visit=set()
            level=0
            dir=[[0,1],[0,-1],[-1,0],[1,0]]
            visit.add((i,j))
            while q:
                for i in range(len(q)):
                    r,c=q.popleft()
                    #print(r,c)
                    if grid[r][c]==0:
                        return level
                    for dr,dc in dir:
                        
                        if (r+dr)<0 or (c+dc)<0 or (r+dr)==row or (c+dc)==col or grid[r+dr][c+dc]==-1 or (r+dr,c+dc) in visit:

                            print((r+dr,c+dc))
                            continue
    
                        q.append((r+dr,c+dc))
                        print("HI")
                        
                        visit.add((r+dr,c+dc))
                level+=1
            return inf

        for i in range(row):
            for j in range(col):
                if grid[i][j]==inf:
                    #("Hi")
                    res[i][j]=bfs(i,j)
        grid=res
        