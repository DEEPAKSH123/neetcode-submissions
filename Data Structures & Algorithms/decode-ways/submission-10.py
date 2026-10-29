class Solution:
    def numDecodings(self, s: str) -> int:
        v=set()
        for i in range(1,27):
            v.add(str(i))
        if len(s)==1:
            if s[0] in v:
                return 1
            return 0
        n=len(s)
        
        dp=[0]*len(s)
        dp[-1]=1 if s[-1]!="0" else 0
        if s[-2] in v:
            dp[-2]+=dp[-1]
        if s[-2:] in v:
            dp[-2]+=1

            
        for i in range(n-3,-1,-1):
            onedigit=s[i]
            twodigit=s[i:i+2]
            a,b=0,0
            if onedigit in v:
                a=dp[i+1]
            if twodigit in v:
                b=dp[i+2]
            dp[i]=a+b
            
        return dp[0]
        