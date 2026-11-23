class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first=cost[-1]
        if len(cost)==1:
            return first
        second=cost[-2]
        for i in range(len(cost)-3,-1,-1):
            tmp=min(cost[i]+first,cost[i]+second)
            first=second
            second=tmp
        return min(first,second)
        