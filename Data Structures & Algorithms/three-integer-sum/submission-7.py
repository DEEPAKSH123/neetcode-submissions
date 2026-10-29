class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        target=0

        nums.sort()
        i=0
        while i < len(nums)-2:
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            
            l=i+1
            r=len(nums)-1
            while l<r:
                value=nums[l]+nums[r]+nums[i]
                if value>target:
                    r-=1
                elif value<target:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
            
            i+=1
        
        return res


        