class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}

        def dfshelper(sum):
            if sum==n:
                return 1
            if sum>n:
                return 0
            if sum in cache:
                return cache[sum]
            onestep=dfshelper(sum+1)
            twostep=dfshelper(sum+2)
            cache[sum] = onestep + twostep
            return cache[sum]
        
        return dfshelper(0)
        