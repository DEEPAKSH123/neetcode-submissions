from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def dfs(i,string):
            if i==len(s):
                if string==t:
                    return 1
                return 0
            skip=dfs(i+1,string)
            include=dfs(i+1,string + s[i])
            return skip+include
        return dfs(0,"")

        