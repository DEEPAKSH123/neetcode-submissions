class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        cache={}
        def dfs(j):
            if j==len(s):
                return True
            if j in cache:
                return cache[j]
            for i in range(len(words)):
                length=len(words[i])
                new=s[j:j+length]
                if new==words[i]:
                    if  dfs(j+length):    
                        cache[j]=True
                        return cache[j]
            cache[j]=False
            return cache[j]
        return dfs(0)

        