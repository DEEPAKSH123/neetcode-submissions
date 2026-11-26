from functools import cache
class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        @cache
        def dfs(i,canBuy):
            if i>=len(nums):
                return 0
            skip= dfs(i+1,canBuy)
            t1=0
            if canBuy:
                t1=dfs(i+1,False)-nums[i]
            else:
                t1=dfs(i+2,True)+nums[i]
            return max(t1,skip)
        return dfs(0,True)

