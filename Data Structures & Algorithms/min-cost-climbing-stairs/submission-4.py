class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[1]*(len(cost)+1)
        n=len(cost)

        first=0
        second=cost[-1]
        for i in range(n-2,-1,-1):
            t=min(cost[i]+second,cost[i]+first)
            first=second
            second=t
        return min(first,second)

        