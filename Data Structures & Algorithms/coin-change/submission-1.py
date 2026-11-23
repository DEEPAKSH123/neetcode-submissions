class Solution:
    def coinChange(self, nums: List[int], amount: int) -> int:
        cache={}
        def dfs(i,target):
            if (i,target) in cache:
                return cache[(i,target)]
            if target>amount:
                return float("inf")
            if target==amount:
                    return 0
            if i>=len(nums):
                return float("inf")
            
            skip=dfs(i+1,target)
            include=1 + dfs(i,target+nums[i])

            cache[(i,target)] = min(skip,include)
            return cache[(i,target)]
        
        return -1 if dfs(0,0)==float("inf") else dfs(0,0)