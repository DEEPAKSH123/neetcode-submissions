class Solution:
    def numDecodings(self, s: str) -> int:
        v=set()
        for i in range(1,27):
            v.add(str(i))
        cache={}
        def dfs(i):
            if i==len(s):
                return 1
            if i>len(s):
                return 0
            if i in cache:
                return cache[i]
            a,b=0,0
            onedigit=s[i]
            twodigit=s[i:i+2]
            if onedigit in v:
                a=dfs(i+1)
            if twodigit in v:
                b=dfs(i+2)
            cache[i]=a+b
            return cache[i]
        return dfs(0)
        