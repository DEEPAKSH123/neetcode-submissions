class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        carry=1
        i=len(nums)-1
        while carry:
            if nums[i]!=9:
                nums[i]=nums[i]+carry
                carry=0
            else:
                if i>0:
                    nums[i]=0
                else:
                    nums[i]=0
                    nums.insert(0,carry)
                    carry=0
            i-=1
        return nums

        