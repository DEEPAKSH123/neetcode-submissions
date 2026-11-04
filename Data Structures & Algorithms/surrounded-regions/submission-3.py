class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit=set()
        row,col=len(board),len(board[0])


        def dfs(i,j):
            if i<0 or j<0 or i>row-1 or j>col-1 or (i,j) in visit or board[i][j] !="O":
                return
            visit.add((i,j))
            board[i][j] = "T"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        def isBorder(i,j):
            if i==0 or j==0 or i==row-1 or j==col-1:
                return True 


        for i in range(row):
            for j in range(col):
                if board[i][j]=="O" and (i,j) not in visit and isBorder(i,j):
                    dfs(i,j)
        
        
        for i in range(row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"

        