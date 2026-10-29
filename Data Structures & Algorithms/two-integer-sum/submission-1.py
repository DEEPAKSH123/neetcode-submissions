class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if (target-nums[i]) not in d:
                d[nums[i]]=i
            else:
                p=[d[(target-nums[i])],i]
                return p
                
