class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l=0
        res=0
        for r in range(1,len(nums)):
            res=max(res,nums[r]-nums[l])
            if nums[r]<nums[l]:
                l=r
        
        return res
        