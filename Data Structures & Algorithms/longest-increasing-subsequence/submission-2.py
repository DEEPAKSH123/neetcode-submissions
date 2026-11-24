
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache={}
        def dfs(i,prev):
            if (i,prev) in cache:
                return cache[(i,prev)]
            if i==len(nums):
                return 0
            skip=dfs(i+1,prev)
            include=0
            if prev<nums[i]:
                include=1+dfs(i+1,nums[i])
            cache[(i,prev)] = max(skip,include)
            return cache[(i,prev)]
        return dfs(0,float("-inf"))