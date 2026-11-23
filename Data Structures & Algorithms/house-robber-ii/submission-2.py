class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        
        def house1(nums):
            if len(nums)==0:
                return 0
            sec=nums[-1]
            if len(nums)==1:
                return sec
            first=max(nums[-2],nums[-1])
            for i in range(len(nums)-3,-1,-1):
                skip=first
                rob=nums[i] + sec
                tmp=max(skip,rob)
                sec=first
                first=tmp
            return first
        
        return max(house1(nums[:-1]),house1(nums[1:]))