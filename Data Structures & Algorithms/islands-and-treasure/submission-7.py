class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row,col=len(grid),len(grid[0])
        q=deque()
        visit=set()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))
        length=0
        res=grid     
        while q:
            length+=1
            for i in range(len(q)):
                r,c=q.popleft()
                neighbours=[(0,1),(1,0),(0,-1),(-1,0)]
                for dr,dc in neighbours:
                    if (r+dr)<0 or (c+dc)<0 or (r+dr)==row or (c+dc)==col or (r+dr,c+dc) in visit or grid[r+dr][c+dc]==-1:
                        continue
                    visit.add((r+dr,c+dc))
                    q.append((r+dr,c+dc))
                    res[r+dr][c+dc]=length
                
        grid=res


        