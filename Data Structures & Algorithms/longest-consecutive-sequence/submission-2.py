class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=1
        if nums==[]:
            return 0

        for n in set(nums):
            if (n-1) not in set(nums):
                length=0
                while (n+length) in nums:
                    length+=1
                res=max(res,length)
        return res