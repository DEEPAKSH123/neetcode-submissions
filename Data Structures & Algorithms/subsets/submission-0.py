class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def dfs(i,res):
            if i==len(nums):
                output.append(res)
                return
            dfs(i+1,res)
            dfs(i+1,res+[nums[i]])
        dfs(0,[])
        return output