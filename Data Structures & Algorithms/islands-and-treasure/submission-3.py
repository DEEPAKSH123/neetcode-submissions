from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        Inf = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            level = 0
            visit = set()
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if i < 0 or j < 0 or i >= row or j >= col or (i, j) in visit or grid[i][j] == -1:
                        continue
                    if grid[i][j] == 0:
                        grid[r][c] = level
                        return
                    visit.add((i, j))
                    q.append((i + 1, j))
                    q.append((i - 1, j))
                    q.append((i, j + 1))
                    q.append((i, j - 1))
                level += 1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == Inf:
                    bfs(r, c)

