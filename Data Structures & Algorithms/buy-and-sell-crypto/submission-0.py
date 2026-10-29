class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l=0
        r=1
        ans=0
        while r<len(nums):
            
            if nums[r]<nums[l]:
                l=r
                r+=1
            else:
                profit=nums[r]-nums[l]
                ans=max(ans,profit)
                r+=1
        return ans

