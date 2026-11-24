from functools import cache 
class Solution:
    
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        @cache
        def dfs(i,curSum):
            if curSum==target:
                return True
            if curSum>target:
                return False
            if i==len(nums):
                return False
            skip=dfs(i+1,curSum)
            include=dfs(i+1,curSum + nums[i])
            return skip or include
        return dfs(0,0)

        