class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            value = nums[l] + nums[r]
            if value == target:
                return [l+1,r+1]
            elif value > target:
                r-=1
            else:
                l+=1
        return [-1,-1]
        