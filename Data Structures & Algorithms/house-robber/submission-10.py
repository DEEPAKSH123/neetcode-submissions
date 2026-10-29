class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # cache ={}
        # def dfs(i):
        #     if i>=len(nums):
        #         return 0
        #     if i in cache:
        #         return cache[i]
            
        #     skip = dfs(i+1)
        #     include = nums[i] + dfs(i+2)
        #     cache[i] = max(skip,include)
        #     return cache[i]
        # return dfs(0)
        if len(nums)==1:
            return nums[0]
        if len(nums) ==2 :
            return max(nums[0],nums[1])
        dp=[0] *(len(nums)+1)
        dp[-1] = 0
        dp[len(nums)-1] = nums[-1]
        

        for i in range(len(nums)-2,-1,-1):
            dp[i] = max(dp[i+1],nums[i]+dp[i+2])
        return dp[0]
