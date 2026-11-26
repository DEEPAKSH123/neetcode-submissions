from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2)>len(s3) :
            return False
        @cache
        def dfs(i,j):
            if i+j==len(s3):
                return True
            if i<len(s1) and  j<len(s2) and s1[i]==s3[i+j] and s2[j]==s3[i+j]:
                return dfs(i+1,j) or dfs(i,j+1)
            elif i<len(s1) and s1[i]==s3[i+j] :
                return dfs(i+1,j)
            elif j<len(s2) and s2[j]==s3[i+j]:
                return dfs(i,j+1)
            else:
                return False
        return dfs(0,0)
            
        