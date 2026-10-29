class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(n,c):
            if n>=len(cost):
                return c

            return min(dfs(n+1,c+cost[n]),dfs(n+2,c+cost[n]))
        return min(dfs(0,0),dfs(1,0))
        