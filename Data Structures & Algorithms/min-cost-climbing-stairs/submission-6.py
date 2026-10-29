class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={}

        def dfshelper(i):
            if i>=len(cost):
                return 0
            if i in cache:
                return cache[i]
            onestep=cost[i]+ dfshelper(i+1)
            twostep=cost[i]+ dfshelper(i+2)
            cache[i] = min(onestep,twostep)
            return cache[i]
        
        if len(cost)==1:
            return dfshelper(0)
        return min(dfshelper(1),dfshelper(0))