class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=min(nums)
        curSum=0
        for n in nums:
            if curSum<0:
                curSum=0
            curSum+=n
            ans=max(curSum,ans)
        return ans
        