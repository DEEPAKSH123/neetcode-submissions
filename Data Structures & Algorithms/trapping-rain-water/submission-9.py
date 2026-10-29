class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        res=0
        r=len(height)-1
        leftmax,rightmax=height[l],height[r]

        while l<r:
            if height[l]<height[r]:
                l+=1
                res+=max(-height[l]+leftmax,0)
                leftmax=max(leftmax,height[l])

            else:
                r-=1
                res+=max(-height[r]+rightmax,0)
                rightmax=max(rightmax,height[r])
        
        return res
        