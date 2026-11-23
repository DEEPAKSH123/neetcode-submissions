class Solution:
    def numDecodings(self, s: str) -> int:  
        valid=set()
        cache={}
        for i in range(1,27):
            valid.add(str(i))

        def dfs(i):
            if i>=len(s):
                return 1
            if i in cache:
                return cache[i]
            
            oneDigit=s[i]
            twoDigit=s[i:i+2]
            t1,t2=0,0
            if oneDigit in valid:
                t1=dfs(i+1)
            if twoDigit in valid and twoDigit!=oneDigit:
                t2=dfs(i+2)
            
            cache[i] = t1+t2
            return cache[i]
        return dfs(0)
            
        