class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n):
            if n==0:
                return 1
            if n<0:
                return 0
            c=0
            c=dfs(n-1)+dfs(n-2)
            return c
        return dfs(n)
        