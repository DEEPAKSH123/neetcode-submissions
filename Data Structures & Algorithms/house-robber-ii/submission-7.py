class Solution:
    def rob(self, num: List[int]) -> int:
        if len(num)==1:
            return num[0]

        cache={}
        def dfs(i,nums):
            nums=tuple(nums)
            if i>=len(nums):
                return 0
            if (i,nums) in cache:
                return cache[(i,nums)]
            
            skip=dfs(i+1,nums)
            include=nums[i]+ dfs(i+2,nums)
            cache[(i,nums)]=max(skip,include)
            return cache[(i,nums)]
        
        a=num[1:]
        b=num[:len(num)-1]
        return max(dfs(0,a),dfs(0,b))
            
        