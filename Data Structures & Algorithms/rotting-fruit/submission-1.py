class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit=set()
        q=deque()
        row,col=len(grid),len(grid[0])
        count=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c]==1:
                    count+=1
        time=0
        if count==0:
            return 0
        if len(q)==0:
            return -1
        
        while q and count:
            for i in range(len(q)):
                r,c=q.popleft()
                neighbours=[(0,1),(1,0),(-1,0),(0,-1)]
                for dr,dc in neighbours:
                    if r+dr<0 or r+dr==row or c+dc<0 or c+dc==col or (r+dr,c+dc) in visit or grid[r+dr][c+dc]==0:
                        continue
                    
                    count-=1
                    print(count)
                    visit.add((r+dr,c+dc))
                    q.append((r+dr,c+dc))
            print(q)
                    
            time+=1
        return time if count==0 else -1