from functools import cache 
class Solution:
    
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        # @cache
        # def dfs(i,curSum):
        #     if curSum==target:
        #         return True
        #     if curSum>target:
        #         return False
        #     if i==len(nums):
        #         return False
        #     skip=dfs(i+1,curSum)
        #     include=dfs(i+1,curSum + nums[i])
        #     return skip or include
        # return dfs(0,0)
        dp=[[False] * (target+1) for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][target] = True
        for i in range(len(nums)-1,-1,-1):
            for j in range(target,-1,-1):
                skip=dp[i+1][j]
                include=False
                if j+nums[i]<=target:
                    include=dp[i+1][j+nums[i]]
                dp[i][j] = skip or include
        return dp[0][0]

        