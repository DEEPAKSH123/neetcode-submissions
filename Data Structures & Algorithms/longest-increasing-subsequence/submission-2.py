class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        ans=0
        def dfs(i,prev):
            if i==len(nums):
                return 0
            skip=dfs(i+1,prev)
            include=0
            if nums[i]>prev:
                include=1+dfs(i+1,nums[i])
            return max(include,skip)
        return dfs(0,-1111)