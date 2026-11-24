class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)
        cache={}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i==len(s):
                return True
            for w in wordDict:
                length=len(w)

                if s[i:i+length] == w:
                    
                    ans = dfs(i+length)
                    if ans:
                        return True
                else:
                    ans=False                    
                
            cache[i] = ans
            return cache[i]
        return dfs(0)
