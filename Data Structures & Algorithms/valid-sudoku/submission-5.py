class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowcheck=defaultdict(set)
        colcheck=defaultdict(set)
        squarecheck=defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                value = board[i][j]
                if value in rowcheck[i] or value in colcheck[j] or value in squarecheck[(i//3,j//3)]:
                    return False
                rowcheck[i].add(board[i][j])
                colcheck[j].add(board[i][j])
                squarecheck[(i//3,j//3)].add(board[i][j])
        
        return True
                