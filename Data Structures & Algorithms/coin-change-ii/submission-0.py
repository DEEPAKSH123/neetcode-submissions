from functools import cache
class Solution:
    def change(self, amount: int, nums: List[int]) -> int:

        @cache
        def dfs(i,total):
            if total>amount:
                return 0
            if i==len(nums):
                return 0
            if total==amount:
                return 1
            skip=dfs(i+1,total)
            include=dfs(i,total+nums[i])
            return skip+include
        return dfs(0,0)
        

