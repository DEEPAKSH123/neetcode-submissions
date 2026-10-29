class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache={}
        def dfshelper(i,j):
            if i==len(text1) or j == len(text2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if text1[i]==text2[j]:
                cache[(i,j)] = 1 + dfshelper(i+1,j+1)
            else:
                cache[(i,j)] = max(dfshelper(i,j+1),dfshelper(i+1,j))
            return cache[(i,j)]

        
        return dfshelper(0,0)