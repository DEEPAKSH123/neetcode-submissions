class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(pos,i,j,visit):
            if pos==len(word):
                return True
            if i<0 or j<0 or i==len(board) or j==len(board[0]) or (i,j) in visit:
                return False 
            if board[i][j]!=word[pos]:
                return False
            visit.add((i,j))
            ans= dfs(pos+1,i+1,j,visit) or dfs(pos+1,i-1,j,visit) or dfs(pos+1,i,j+1,visit) or dfs(pos+1,i,j-1,visit)
            visit.remove((i,j))
            return ans

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    ans=dfs(0,i,j,set())
                    if ans:
                        return True
        return False               
        