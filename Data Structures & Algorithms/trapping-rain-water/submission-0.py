class Solution:
    def trap(self, nums: List[int]) -> int:
        l=0
        ans=0
        r=len(nums)-1
        leftmax=nums[l]
        rightmax=nums[r]
        while l<r:
            if nums[l]<nums[r]:
                l+=1
                leftmax=max(leftmax,nums[l])
                ans+=(leftmax-nums[l])
            else:
                r-=1
                rightmax=max(rightmax,nums[r])
                ans+=(rightmax-nums[r])
        return ans
        