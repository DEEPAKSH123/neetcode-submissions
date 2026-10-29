class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                total=nums[i]+nums[r]+nums[l]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l+=1
                    while l<len(nums) and nums[l]==nums[l-1]:
                        l+=1
                    
        return res
        