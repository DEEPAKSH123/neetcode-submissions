from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i,prev):
            if i==len(nums):
                return 0
            skip=dfs(i+1,prev)
            include=0
            if prev<nums[i]:
                include=1+dfs(i+1,nums[i])
            return max(skip,include)
        return dfs(0,float("-inf"))