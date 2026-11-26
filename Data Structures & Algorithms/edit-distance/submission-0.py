from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i,j):
            if i==len(word1) and j==len(word2):
                return 0

            if i<len(word1) and j<len(word2) and word1[i]==word2[j]:
                return dfs(i+1,j+1)
            else:
                insert,replace,delete=101,101,101
                if j<len(word2):
                    insert=1+dfs(i,j+1)
                if i<len(word1):
                    delete=1+dfs(i+1,j)
                if i<len(word1) and j<len(word2):
                    replace=1+dfs(i+1,j+1)
                return min(insert,replace,delete)
        return dfs(0,0)
