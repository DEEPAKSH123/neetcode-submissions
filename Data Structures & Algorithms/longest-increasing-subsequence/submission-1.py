from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, prev):
            if i == len(nums):
                return 0

            # Option 1: Skip the current element
            a = dfs(i + 1, prev)
            
            # Option 2: Include the current element if it forms an increasing subsequence
            b = 0
            if nums[i] > prev:
                b = 1 + dfs(i + 1, nums[i])
            
            return max(a, b)
        
        return dfs(0, float("-inf"))
