class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        part=[0,0]
        cache={}
        def dfs(i):
            if i==len(nums):
                if part[0]==part[1]:
                    return True
                return False
            if i in cache:
                return cache
            part[0]+=nums[i]
            a=dfs(i+1)
            part[0]-=nums[i]
            part[1]+=nums[i]
            b=dfs(i+1)
            part[1]-=nums[i]
            return a or b
        return dfs(0)