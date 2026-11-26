from functools import cache
class Solution:
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visit=set()
        res=0
        @cache
        def dfs(i,j):
            if i<0 or j<0 or i==len(matrix) or j==len(matrix[0]) or (i,j) in visit:
                return 0
            t1,t2,t3,t4=1,1,1,1
            visit.add((i,j))
            if i+1<len(matrix) and matrix[i+1][j]>matrix[i][j]:
                t1=1+dfs(i+1,j)
            if i>=1 and matrix[i-1][j]>matrix[i][j]:
                t2=1+dfs(i-1,j)
            if j+1<len(matrix[0]) and matrix[i][j+1]>matrix[i][j]:
                t3=1+dfs(i,j+1)
            if j>=1 and matrix[i][j-1]>matrix[i][j]:
                t4=1+dfs(i,j-1)
                    
            ans= max(t1,t2,t3,t4)
            visit.remove((i,j))
            return ans
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res=max(res,dfs(r,c))
        return res
            