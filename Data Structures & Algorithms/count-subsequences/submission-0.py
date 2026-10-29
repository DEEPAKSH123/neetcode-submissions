class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache={}

        def dfs(i,word):
            if (i,word) in cache:
                return cache[(i,word)]
            if i==len(s):
                if word==t:
                    return 1
                return 0
            skip = dfs(i+1,word)
            include = dfs(i+1,word+s[i])
            cache[(i,word)] = skip + include
            return cache[(i,word)]
        return dfs(0,"")
        