class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        r=len(nums)-1
        ans=float("inf")
        while l<=r:
            if nums[l]<=nums[r]:
                ans=min(ans,nums[l])
                return ans
            m=(l+r)//2
            if nums[m]>=nums[l]:
                l=m+1
            else:
                ans=min(ans,nums[m])
                r=m-1
        return ans
        