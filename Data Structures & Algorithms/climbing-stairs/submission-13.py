class Solution:
    def climbStairs(self, n: int) -> int:
        # cache={}
        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
        #     if i>n:
        #         return 0
        #     if i==n:
        #         return 1
        #     oneStep=dfs(i+1)
        #     twoStep=dfs(i+2)
        #     cache[i] = oneStep + twoStep
        #     return cache[i]
        # return dfs(0)


        first,sec=1,1
        for i in range(n-2,-1,-1):
            temp = first + sec
            sec = first
            first = temp
        return first
        