class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i==len(cost):
                return 0
            if i>len(cost):
                return 10000
            a1=cost[i]+dfs(i+1)
            a2=cost[i]+dfs(i+2)

            return min(a1,a2)
        return min(dfs(0),dfs(1))
        