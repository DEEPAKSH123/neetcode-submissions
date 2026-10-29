class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for index,value in enumerate(nums):
            diff=target-value
            if diff in d:
                return [d[diff],index]
            d[value]=index
        return -1
        