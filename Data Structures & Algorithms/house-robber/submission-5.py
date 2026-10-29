class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}


        def dfshelper(i):
            if i>=len(nums):
                return 0
            if i in cache:
                return cache[i]
            include=nums[i]+dfshelper(i+2)
            skip=dfshelper(i+1)
            cache[i] = max(skip,include)
            return cache[i]
        
        return dfshelper(0)
        