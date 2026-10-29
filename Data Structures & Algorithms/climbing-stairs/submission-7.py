class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        first=1
        second=1
        for i in range(n-2,-1,-1):
            temp=first+second
            first=second
            second=temp

        return second