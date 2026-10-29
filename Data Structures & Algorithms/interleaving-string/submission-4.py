class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)>len(s1)+len(s2):
            return False
        cache={}

        def dfs(i,j):
            if i==len(s1) and j==len(s2):
                return True
            a1,a2,a3=False,False,False
            a4=True
            if (i,j) in cache:
                return cache[(i,j)]
            if i<len(s1) and j<len(s2) and (i+j)<len(s3) and s1[i]==s3[i+j] and s2[j]==s3[i+j]:
                a1=dfs(i+1,j) or dfs(i,j+1)
            elif i<len(s1) and (i+j)<len(s3) and s1[i]==s3[i+j]  :
                a2=dfs(i+1,j)
            elif j<len(s2) and (i+j)<len(s3) and s2[j]==s3[i+j]  :
                a3=dfs(i,j+1)
            else:
                return False
            cache[(i,j)]= (a1 or a2 or a3)
            return cache[(i,j)]

                

        return dfs(0,0)
        