class Solution:
    def climbStairs(self, n: int) -> int:
        #cache=[1]*(n+1)
        a=1
        b=1
        for i in range(n-1):
            t=a
            a=a+b
            b=t
        return a
        