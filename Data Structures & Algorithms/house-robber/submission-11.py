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
        sec = 0
        first = nums[-1]
        

        for i in range(len(nums)-2,-1,-1):
            temp = max(first,nums[i]+sec)
            sec= first
            first = temp
        return temp
