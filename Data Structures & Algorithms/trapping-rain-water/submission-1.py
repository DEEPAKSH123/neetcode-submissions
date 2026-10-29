class Solution:
    def trap(self, nums: List[int]) -> int:
        left=[0]*len(nums)
        ans=0
        right=[0]*len(nums)
        left[0]=nums[0]
        right[-1]=nums[-1]
        for i in range(1,len(nums)):
            left[i]=max(left[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            right[i]=max(right[i+1],nums[i])
        for i in range(len(nums)):
            a=left[i-1] if i>=1 else 0
            b=right[i+1] if i+1<len(nums) else 0
            if nums[i]<min(a,b):
                ans+=(min(a,b)-nums[i])
        return ans

         