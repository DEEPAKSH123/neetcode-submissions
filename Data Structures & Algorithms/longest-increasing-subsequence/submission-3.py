class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        ans=0
        cache={}
        def dfs(i,prev):
            if i==len(nums):
                return 0
            if (i,prev) in cache:
                return cache[(i,prev)]
            skip=dfs(i+1,prev)
            include=0
            if nums[i]>prev:
                include=1+dfs(i+1,nums[i])
            cache[(i,prev)]=max(include,skip)
            return cache[(i,prev)]
        return dfs(0,-1111)