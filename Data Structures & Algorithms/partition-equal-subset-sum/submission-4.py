class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        cache={}
        
        def memo(i,sum):
            if i==len(nums):
                return False
            if sum==0:
                return True
            if (i,sum) in cache:
                return cache[(i,sum)]
            skip=memo(i+1,sum)
            include=False
            if sum-nums[i]>=0:
                include=memo(i+1,sum-nums[i])
            cache[(i,sum)] = skip or include
            return cache[(i,sum)]
        
        return memo(0,sum(nums)//2)