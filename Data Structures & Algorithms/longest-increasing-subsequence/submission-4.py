class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache={}
        def dfs(i,prev):
            if i==len(nums):
                return 0
            if (i,prev) in cache:
                return cache[(i,prev)]
            ans=0
            for j in range(i,len(nums)):
                if nums[j]>prev:
                    ans=max(ans,1+dfs(j+1,nums[j]))
            cache[(i,prev)]=ans
            return cache[(i,prev)]
        return dfs(0,-1111)