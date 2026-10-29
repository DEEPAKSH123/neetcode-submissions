class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        dp=[0]*(n)
        first=nums[-1]
        second=max(nums[-2],nums[-1])
        for i in range(n-3,-1,-1):
            temp=max(nums[i]+first,second)
            first=second
            second=temp
            
        return second
        